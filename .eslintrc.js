module.exports = {
  extends: ['airbnb-base', 'plugin:vue/recommended'],
  env: {
    browser: true,
    jquery: true,
  },
  rules: {
    'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'linebreak-style': 0,  // TODO: rm after finish work
  },
  parserOptions: {
    parser: "babel-eslint",
    ecmaVersion: 2017,
    sourceType: "module",
  },
  plugins: ['vue'],
};
