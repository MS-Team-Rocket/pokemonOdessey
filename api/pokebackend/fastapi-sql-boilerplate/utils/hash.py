from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated="auto")

class Hash():
    def bcrypt(password: str):
        """
        Hashes a password using bcrypt.

        Args:
            password (str): The password to be hashed.

        Returns:
            str: The hashed password.
        """
        return pwd_cxt.hash(password)

    def verify(hashed_password, plain_password):
        """
        Verify the plain password against the hashed password.
        
        Parameters:
            hashed_password (str): The hashed password to compare against.
            plain_password (str): The plain password to verify.
        
        Returns:
            bool: True if the plain password matches the hashed password, False otherwise.
        """
        return pwd_cxt.verify(plain_password, hashed_password)