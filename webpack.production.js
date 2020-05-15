/* eslint-disable import/no-extraneous-dependencies */
const merge = require('webpack-merge');
const TerserPlugin = require('terser-webpack-plugin');
const OptimizeCSSAssetsPlugin = require('optimize-css-assets-webpack-plugin');
const { BundleAnalyzerPlugin } = require('webpack-bundle-analyzer');
const common = require('./webpack.common');

module.exports = merge(common, {
  stats: 'errors-warnings',
  optimization: {
    minimizer: [
      new TerserPlugin(),
      new OptimizeCSSAssetsPlugin({}),
    ],
  },
  plugins: [
    new BundleAnalyzerPlugin({
      analyzerMode: 'static',
      openAnalyzer: false,
    }),
  ],
});
