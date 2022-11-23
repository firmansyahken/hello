const char = document.getElementById("char");
const nameChar = document.getElementById("name");
const text = document.getElementById("text");
const bg = document.querySelector(".background");
const preloader = document.querySelector(".preloader");
const data = "story.json";
const stories = [];

var current = 0;

const fetchStory = () => {
  fetch(data)
    .then((r) => r.json())
    .then((data) => {
      stories.push(data);
      renderData();
      current += 1;
    });
};

fetchStory();

const handleStory = () => {
  renderData();
  if (current < stories[0].stories.length - 1) {
    current += 1;
    return;
  } else {
    current = 0;
  }
};

const renderData = () => {
  const character = stories[0].characters;
  const background = stories[0].background;
  const story = stories[0].stories;
  nameChar.innerText = story[current].name;
  text.innerText = story[current].message;
  char.setAttribute("src", character[story[current].image]);
  bg.setAttribute("src", background[story[current].background]);
};

document.querySelector(".wrapper").addEventListener("click", handleStory);

function start() {
  preloader.classList.add("disable");
  const ost = new Audio("assets/ost.mp3");
  ost.currentTime = 18;
  ost.loop = true,
    setTimeout(() => {
      preloader.style.display = "none";
    }, 1000);
    setTimeout(() => {
      ost.play();
    }, 1500)
}