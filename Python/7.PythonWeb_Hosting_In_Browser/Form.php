<!DOCTYPE html>
<html>
<head>
    <title> Form</title>

    <style>
        .Button
        {
          color : white;
          background : linear-gradient(to left, red, blue);  
          font-size: 20px;
        }

    </style>
</head>

<body>
    <div align="center">
        <h1>Welcom on Python-WebApplication</h1>
        <form action="SignUp.py" method="post">
            <b>Enter Your Name : </b>
            <input type="text" name="name" placeholder="Name" required><br>
            <b>Enter Address :</b>
            <input type="text" name="address" placeholder="Address" required><br>

            <b>Select Gender :</b>
            <input type="radio" name="gender" value="Male" required>Male
            <input type="radio" name="gender" value="Female" required>Felmale
            <input type="radio" name="gender" value="Other" required>Other <br>

            <b>Enter Password :</b>
            <input type="password" name="password"><br>

            <b>Select Country :</b>
            <select name="country" id="">
                <option value="India">India</option>
                <option value="Nepal">Nepal</option>
                <option value="China">China</option>
            </select>
            <hr color=blue>

            <input type="submit" name="submit" value="Sign Up" class = "Button"><br>
            <input type="reset" name="reset" value="Reset" class = "Button">



        </form>
    </div>
</body>

</html>