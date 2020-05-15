/* eslint-disable import/no-extraneous-dependencies */
const merge = require('webpack-merge');
const { BundleAnalyzerPlugin } = require('webpack-bundle-analyzer');
const common = require('./webpack.common');

module.exports = merge(common, {
  output: {
    publicPath: 'http://localhost:8080/static/',
  },
  devServer: {
    overlay: true,
    hot: true,
    publicPath: 'http://localhost:8080/static',
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, PATCH, OPTIONS',
      'Access-Control-Allow-Headers': 'X-Requested-With, content-type, Authorization',
    },
    port: 8080,
    stats: 'errors-warnings',
  },
  plugins: [
    new BundleAnalyzerPlugin({
      openAnalyzer: false,
    }),
  ],
});
