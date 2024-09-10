const {default: daisyui} = require('daisyui');

/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: "jit",
  content: ["./app/templates/**/*.html"],
  theme: {
    extend: {},
  },
  plugins: [
    require("@tailwindcss/typography"),
    require("daisyui")
  ],
  daisyui: {
    themes: ["dark", "light"],
    styled: true
  },
  darkMode: 'class'
}

