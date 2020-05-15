/* eslint-disable import/no-extraneous-dependencies */
const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const webpack = require('webpack');
const postcssPresetEnv = require('postcss-preset-env');
const BundleTracker = require('webpack-bundle-tracker');
const VueLoaderPlugin = require('vue-loader/lib/plugin');
const StyleLintPlugin = require('stylelint-webpack-plugin');
const MomentLocalesPlugin = require('moment-locales-webpack-plugin');

const devMode = process.env.NODE_ENV !== 'production';
console.log('devMode', devMode);
module.exports = {
  entry: {
    // ice: path.resolve(__dirname, 'src', 'ice', 'js', 'ice.js'),
    app: path.resolve(__dirname, 'src', 'js', 'app.js'),
  },
  output: {
    filename: 'js/[name]-[hash].js',
    path: path.resolve(__dirname, 'staticfiles'),
    publicPath: '/static/',
  },
  devtool: 'source-map',
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader',
      },
      {
        test: /\.js$/,
        exclude: /(node_modules|bower_components)/,
        use: [{
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env'],
          },
        }],
      },
      {
        enforce: 'pre',
        test: /\.(js|vue)$/,
        loader: 'eslint-loader',
        exclude: /node_modules/,
      },
      {
        test: /\.css/,
        use: [
          devMode ? 'style-loader' : MiniCssExtractPlugin.loader,
          {
            loader: 'css-loader',
            options: {
              sourceMap: true,
            },
          },
          {
            loader: 'postcss-loader',
            options: {
              sourceMap: true,
              ident: 'postcss',
              plugins: () => [postcssPresetEnv()],
            },
          },
        ],
      },
      {
        test: /\.(scss|sass)/,
        use: [
          devMode ? 'style-loader' : MiniCssExtractPlugin.loader,
          {
            loader: 'css-loader',
            options: {
              sourceMap: true,
            },
          },
          {
            loader: 'postcss-loader',
            options: {
              sourceMap: true,
              ident: 'postcss',
              plugins: () => [postcssPresetEnv()],
            },
          },
          {
            loader: 'sass-loader',
            options: {
              sourceMap: true,
            },
          },
        ],
      },
      {
        test: /\.(woff|woff2|eot|ttf|otf|png|jpg|gif|svg)$/,
        use: [
          {
            loader: 'file-loader',
            options: {
              name: '[path][name].[ext]',
            },
          },
        ],
      },
      {
        test: require.resolve('jquery'),
        use: [{
          loader: 'expose-loader',
          options: 'jQuery',
        }, {
          loader: 'expose-loader',
          options: '$',
        }],
      },
    ],
  },
  plugins: [
    new webpack.ProvidePlugin({
      $: 'jquery',
      jQuery: 'jquery',
    }),
    new MiniCssExtractPlugin({
      filename: 'css/[name]-[hash].css',
      chunkFilename: 'css/[id].css',
    }),
    new webpack.NamedModulesPlugin(),
    new webpack.HotModuleReplacementPlugin(),
    new BundleTracker({
      filename: './webpack-stats.json',
    }),
    new VueLoaderPlugin(),
    new MomentLocalesPlugin({
      localesToKeep: ['ru'],
    }),
  ],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src', 'js'),
    },
  },
};
