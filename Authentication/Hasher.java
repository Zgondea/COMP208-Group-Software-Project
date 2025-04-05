import java.util.Base64;
import java.security.MessageDigest;
import java.security.SecureRandom;
import java.security.NoSuchAlgorithmException;

public class Hasher{

    /**  
     * Method to Hash the Password using the SHA-256 algorithm.
     * 
     * @param password the password to be hashed.
     * @return Return the salt and hashed password together separated with "$".
     */
    public String hashPassword(String password){
        try{
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            
            // Generate a random salt.
            SecureRandom random = new SecureRandom();
            byte[] salt = new byte[16];
            random.nextBytes(salt); 
            md.update(salt);
            byte[] hashedBytes = md.digest(password.getBytes());
            
            // Combine salt and hashed password, then encode in Base64 for storage.
            String saltBase64 = Base64.getEncoder().encodeToString(salt);
            String hashedPassword = Base64.getEncoder().encodeToString(hashedBytes);
            
            // Return the salt and hashed password together separaetd with "$".
            // Returned as: salt$hashedPassword
            return saltBase64 + "$" + hashedPassword;
        } 
        catch(NoSuchAlgorithmException e){
            e.printStackTrace();
        }
        return null;
    }

    /**  
     * Method to verify the password by:
     *  1) Hashing the inputted password and
     *  2) Comparing it with the stored hash
     * 
     * @param password the inputted password.
     * @param storedPassword the stored Password.
     * @return true if the password matches, false otherwise.
     */
    public boolean checkPassword(String password, String storedPassword){
        try{
            // Split stored password into salt and hash.
            String[] parts = storedPassword.split("\\$");
            String saltBase64 = parts[0];
            String storedHash = parts[1];
            
            // Decode the salt and hash.
            byte[] salt = Base64.getDecoder().decode(saltBase64);
            byte[] storedHashBytes = Base64.getDecoder().decode(storedHash);
            
            // Hash the inputted password.
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            md.update(salt);
            byte[] hashBytes = md.digest(password.getBytes());
            
            // Compare the newly generated hash with the stored one.
            return MessageDigest.isEqual(hashBytes, storedHashBytes);
        } 
        catch(Exception e){
            e.printStackTrace();
        }
        return false;
    }
}
