"use strict";
// This file is required by karma.conf.js and loads recursively all the .spec and framework files

Liferay.Loader.define("example-angular-liferay@0.0.0/test", ['module', 'exports', 'require', 'example-angular-liferay$zone.js/dist/zone-testing', '@example-angular-liferay$angular/core/testing', '@example-angular-liferay$angular/platform-browser-dynamic/testing'], function (module, exports, require) {
  var define = undefined;
  Object.defineProperty(exports, "__esModule", { value: true });
  require("example-angular-liferay$zone.js/dist/zone-testing");
  var testing_1 = require("@example-angular-liferay$angular/core/testing");
  var testing_2 = require("@example-angular-liferay$angular/platform-browser-dynamic/testing");
  // First, initialize the Angular testing environment.
  testing_1.getTestBed().initTestEnvironment(testing_2.BrowserDynamicTestingModule, testing_2.platformBrowserDynamicTesting());
  // Then we find all the tests.
  var context = require.context('./', true, /\.spec\.ts$/);
  // And load the modules.
  context.keys().map(context);
  //# sourceMappingURL=test.js.map
});
//# sourceMappingURL=test.js.map