


<!-- PROJECT LOGO -->
<div align="center">

<h2 align="center">Atmospheric Composition Variable Standard Name Checker</h2>

  <p align="center">
    <br />
    <a href="https://github.com/ekqian/acvsn-checker"><strong>Explore the docs »</strong></a>
    <br />
    <a href="https://github.com/ekqian/acvsn-checker">View Demo</a>
    ·
    <a href="https://github.com/ekqian/acvsn-checker/issues">Report Bug</a>
    ·
    <a href="https://github.com/ekqian/acvsn-checker/issues">Request Feature</a>
    <br /><br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li><a href="#installation">Installation</a></li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#check-name">Check Name</a></li>
        <li><a href="#check-file">Check File</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

The ACVSN checker is a command line application that checks if a standard name meets the guidelines under the Atmospheric Composition Variable Standard Name Convention (ACVSNC). 

For complete documentation on ACVSNC, refer to [https://www.earthdata.nasa.gov/esdis/esco/standards-and-practices/acvsnc](https://www.earthdata.nasa.gov/esdis/esco/standards-and-practices/acvsnc). 

<br>

<!-- Installation -->
## Installation

To install the package onto your local device, run the following command in the terminal.

Make sure that Python version 3.4 or newer is installed.

   ```sh
   pip install acvsn-checker==0.1.5
   ```
<br>

<!-- USAGE EXAMPLES -->
## Usage

The program has two main functionalities; it can check if a single standard name is valid and it can check if the standard names in an ICARTT (.ict) file are valid.

### Check Name
To check a standard name is valid, run the following command in the terminal:

```sh
checker check-name *standardname
   ```
*`*standardname
`is a user-inputted standard name.*

### Check File
To check the header of a file, run the following command in the terminal:

```sh
checker check-file *filepath
   ```
*`*filepath
`is the absolute path that points to the .ict file.*

<br>

<!-- LICENSE -->
## License

See `LICENSE.txt` for more information.

<br>

<!-- CONTACT -->
## Contact

Email: [ekqian@seas.upenn.edu](ekqian@seas.upenn.edu)

Github: [https://github.com/ekqian](https://github.com/ekqian)
