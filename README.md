# python_80s_musictrivia
<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/nater9ster/python_80s_musictrivia">
  </a>

<h3 align="center">80's Music Trivia!</h3>

  <p align="center">
    This is a game I created in Python that tests your knowledge of songs from the 80's! <br>
    <br />
    <a href="https://github.com/nater9ster/python_80s_musictrivia"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/nater9ster/python_80s_musictrivia">View Demo</a>
    ·
    <a href="https://github.com/nater9ster/python_80s_musictrivia/issues">Report Bug</a>
    ·
    <a href="https://github.com/nater9ster/python_80s_musictrivia/issues">Request Feature</a>
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
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
 <p>The key features: The user gets to play a quiz type game by guessing which 80’s music artist sang the lyrics shown to them. If they guess correctly they score 100 points. If incorrect they will be shown 3 artists to choose from, if they guess the correct one out of the three they receive 50 points. Once the user reaches 1000 points, they win the game!</p>
      <p>The design is fairly simple using a class Question to initiate randomly each question as an object. The attributes are (self, lyrics, correct_answer, options) I took these 3 attributes of each object and put them into a large list. I listed them each as Question(“lyrics”, “correct_answer”, [“option1”, “option2”, “option3”])
	This allowed me to randomly iterate through the questions list. I had a difficult time figuring this out, but was successful using a for loop “for Question in questions”.
	Another challenge at first was making the case not matter, because I was using different cases in lyrics and correct_answer and needed to make sure the case wouldn’t matter from the user input. I.e. Motley Crue = motley crue 
	I was able to use .lower everywhere user input was made, I.e. answer.lower and correct_answer.lower which made it not matter what case was used as long as the characters matched.</p>
 <p>I learned how to implement Class and lists and enjoyed finally getting the game to work out! A fun additional feature would be to implement a 10 second timer giving the user urgency to answer the question. Also making the actual sound byte come up when the lyric comes up, or perhaps even replacing the lyric shown on the screen with just the actual lyric as a sound byte.</p>
<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* Python!

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/nater9ster/python_80s_musictrivia.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/nater9ster/python_80s_musictrivia/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Nate Rollins - nater9ster@gmail.com

Project Link: [https://github.com/nater9ster/python_80s_musictrivia](https://github.com/nater9ster/python_80s_musictrivia)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/nater9ster/python_80s_musictrivia.svg?style=for-the-badge
[contributors-url]: https://github.com/nater9ster/python_80s_musictrivia/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/nater9ster/python_80s_musictrivia.svg?style=for-the-badge
[forks-url]: https://github.com/nater9ster/python_80s_musictrivia/network/members
[stars-shield]: https://img.shields.io/github/stars/nater9ster/python_80s_musictrivia.svg?style=for-the-badge
[stars-url]: https://github.com/nater9ster/python_80s_musictrivia/stargazers
[issues-shield]: https://img.shields.io/github/issues/nater9ster/python_80s_musictrivia.svg?style=for-the-badge
[issues-url]: https://github.com/nater9ster/python_80s_musictrivia/issues
[license-shield]: https://img.shields.io/github/license/nater9ster/python_80s_musictrivia.svg?style=for-the-badge
[license-url]: https://github.com/nater9ster/python_80s_musictrivia/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/naterollins
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
