<a name="readme-top"></a>
<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Stargazers][stars-shield]][stars-url]
[![support][buy-shield]][buy-url]
[![Total Downloads](https://img.shields.io/github/downloads/GarikDog/autobake_tools/total?style=for-the-badge&logo=appveyor)](https://github.com/GarikDog/autobake_tools/releases)
[![Release][release-shield]][release-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="[https://github.com/othneildrew/Best-README-Template](https://github.com/GarikDog/autobake_tools/)">
    <img src="images/logo_f.png" alt="Logo" width="200" height="200">
  </a>

  <h3 align="center">Auto-bake Tools</h3>

  <p align="center">
    Blender Add-on for Automatic Bevel Shader - Normal Map Baking
    <br />
      easy to use
    <br />
      useful for 3D artists
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#explanation-of-what-addon-code-does">Explanation of what the addon code does</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project



An easy to use Blender Add-on that allows you to bake Bevel Shader to the Normal Map, Ambient Occlusion to the AO Map in fully automatic mode. 




* If You are working in Blender, this will save you a lot of time!
* If You're not working in Blender but need to bake your bevels, this will save you even more time!

![](https://github.com/GarikDog/autobake_tools/blob/main/images/autobake_bevel_demo.gif)
![](https://github.com/GarikDog/autobake_tools/blob/main/images/baking_ao_demo.gif)
![](https://github.com/GarikDog/autobake_tools/blob/main/images/substance_demo.gif)
[![Product Name Screen Shot][product-screenshot]](https://github.com/GarikDog/autobake_tools/blob/main/images/screenshot.png)


<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![bpy][project/bpy]][bpy-url]


<!-- GETTING STARTED -->
## Getting Started



### Prerequisites


First You need to install Blender (You need the ***3,0,1*** or newer)

* Download the last blender release: 

* [![blender][blender.org]][blender-url]

### Installation

1. Download latest release of Autobake Tools:

* [![Release][release-shield]][release-url]

* You also can ❤:

* [![support][buy-shield]][buy-url]

2. Run Blender

3. Go to ***Edit>Preferences Add-ons tab.***

4. At the top right of the Blender Preferences window, push the ***install...*** button.

5. Find the ***downloaded zip with Auto-bake Tools*** in file manager that appeared, select and click ***Install Add-on***.

6. Next, use the search in the Blender Preferences window (Directly under the ***Install...*** button), find the addon by name.

7. Check the box next to the found Add-on.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage
1. Select an object that need to bake in the scene. ***(Must be UV unwrapped)***

2. If an object is selected, the ***Auto-bake Tools*** Panel will become available.

3. Go to ***Auto-bake Tools*** Panel

4. Push the ***Create Bake Environment*** button

5. Correct Values:
* ***Image Width*** - Bake Image width
* ***Image Height*** - Bake Image height

For Bevel:
* ***Glossy Preview*** - Sets the glossy shader to visually display Bevel effect
* ***Bevel Samples*** - Number of rays to trace per belel shader evaluation.
* ***Bevel Radius*** - radius of traced bevels (in meters by default)

For AO:
* ***AO Distance*** - distance of AO tracing
* ***AO Samples*** - Number of rays to trace per Ambient Occlusion evaluation
* ***AO Exponentiation*** - Exponentiation value of AO to increase contrast


6. Push the ***Bake Normal and Show*** button for Bevel or ***Bake AO and Show*** for AO
7. Wait... And That's All! You may save the Bake result Normal Map/AO Map in Image Window that appeared

You can look at this gif:

![](https://github.com/GarikDog/autobake_tools/blob/main/images/baking_bevel.gif)


***Important additional information:***

It is advisable to check if GPU Render is available for Cycles.

If not available, go to Edit>Preferences System tab
In it, select the CUDA subtab and uncheck / check the boxes next to your video card name and near the processor name.

After these steps, GPU Compute will be available in most cases (If the hardware is not quite ancient)

***GPU Compute for Cycles is extremely important and greatly overclocks the render, please keep in mind!***


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- EXPLORATION -->
## Explanation of what the addon code does

***Create Bake Environment operator:***

* ***Shading setup:***
1. Sets the Render Engine to ***Cycles***

2. Sets the Render Feature Set to ***Supported***

3. Trying to set the Render Device to ***GPU***

4. Sets the ***Bake Multires*** to False

5. Sets the ***Selected to Active*** to False

* ***Material Setup:***
1. ***Creates Material*** (if selected object have not material)

2. Sets the ***Use Nodes*** to True

* ***Shader Editor setup:***

1. Cleares Nodes

2. Creates, places and conneсts ***Glossy BSDF, Diffuse BSDF, Material Output, Bevel node, Image Texture node, Ambient Occlusion, Math(Power)***

***Bake Normal and Show operator:***

* Creates the ***Image*** with ***custom _n name ending***

* Runs default  blender ***Bake*** operator with type ***Normal***

***Bake AO and Show operator:***

* Creates the ***Image*** with ***custom _ao name ending***

* Runs default  blender ***Bake*** operator with type ***DIFFUSE***

* Opens the window with the Result

***Glossy preview,
Image Width,
Image Height,
Bevel Samples,
Bevel Radius,
AO Distance,
AO Samples,
AO Exponentiation*** - custom properties. It's implementation allows you to change the values ​​at any time. The nodes will get them anyway.




<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

-  Add a multimesh bake



See [open issues](https://github.com/GarikDog/autobake_tools/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the APACHE-2.0 License. See [LICENSE.md](https://github.com/GarikDog/autobake_tools/blob/main/LICENSE.md) for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

Igor Subachev (GarikDog) - [Discord](https://discordapp.com/users/GarikDog#7847) - sobakapppoe@gmail.com

Project Link: [https://github.com/GarikDog/autobake_tools](https://github.com/GarikDog/autobake_tools)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* Thanks to [Steven Wyatt](https://www.udemy.com/user/steven-wyatt-2/) for a great course on bpy development


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/GarikDog/autobake_tools.svg?style=for-the-badge
[contributors-url]: https://github.com/GarikDog/autobake_tools/graphs/contributors
[release-url]: https://github.com/GarikDog/autobake_tools/releases/latest
[release-shield]: https://img.shields.io/github/release/GarikDog/autobake_tools.svg?style=for-the-badge
[stars-shield]: https://img.shields.io/github/stars/GarikDog/autobake_tools.svg?style=for-the-badge
[stars-url]: https://github.com/GarikDog/autobake_tools/stargazers
[issues-shield]: https://img.shields.io/github/issues/GarikDog/autobake_tools.svg?style=for-the-badge
[issues-url]: https://github.com/GarikDog/autobake_tools/issues
[license-shield]: https://img.shields.io/github/license/GarikDog/autobake_tools.svg?style=for-the-badge
[license-url]: https://github.com/GarikDog/autobake_tools//blob/main/LICENSE.md
[product-screenshot]: images/screenshot.png
[product-gif-demo]: images/baking_bevel.gif

[blender-url]: https://www.blender.org/
[blender.org]: https://img.shields.io/badge/blender-0769AD?style=for-the-badge&logo=blender&logoColor=orange
[bpy-url]: https://pypi.org/project/bpy/
[project/bpy]: https://img.shields.io/badge/bpy-0769AD?style=for-the-badge&logo=pypi&logoColor=white





[buy-shield]:https://img.shields.io/badge/Blender%20Market-Support%20with%20a%20purchase-orange?style=for-the-badge&logo=appveyor
[buy-url]:https://www.blendermarket.com/products/autobake-tools
