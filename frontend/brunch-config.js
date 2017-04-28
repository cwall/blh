
module.exports = {
  paths: {
    public: '../static',
    watched: [
      'app',
      'assets',
      'sass',
      'vendor',
    ]
  },
  files: {
    javascripts: {
      joinTo: {
        'js/full.js': /^app(\/|\\)js/,
        'js/vendor.js': /^(vendor|bower_components)/,
        'test/js/test.js': /^test(\/|\\)(?!vendor)/,
        'test/js/test-vendor.js': /^test(\/|\\)(?=vendor)/
      }
    },
    stylesheets: {
      joinTo: {
        'css/base.css': /^app/,
        'css/vendor.css': /^(vendor|bower_components)/
      }
    },
    templates: {joinTo: 'full.js'}
  },

  sourceMaps: false,

  // wrap non-vendor files in an IIFE
  wrapper: function(path, data, vendor) {
    return vendor ? data : "(function() {\n  'use strict';\n " + data + " \n})();\n\n";
  }
 
}
