"use strict";

Liferay.Loader.define("example-angular-liferay@0.0.0/main", ['module', 'exports', 'require', '@example-angular-liferay$angular/core', '@example-angular-liferay$angular/platform-browser-dynamic', './app/app.module', './environments/environment'], function (module, exports, require) {
    var define = undefined;
    Object.defineProperty(exports, "__esModule", { value: true });
    var core_1 = require("@example-angular-liferay$angular/core");
    var platform_browser_dynamic_1 = require("@example-angular-liferay$angular/platform-browser-dynamic");
    var app_module_1 = require("./app/app.module");
    var environment_1 = require("./environments/environment");
    if (environment_1.environment.production) {
        core_1.enableProdMode();
    }
    platform_browser_dynamic_1.platformBrowserDynamic().bootstrapModule(app_module_1.AppModule).catch(function (err) {
        return console.log(err);
    });
    //# sourceMappingURL=main.js.map
});
//# sourceMappingURL=main.js.map