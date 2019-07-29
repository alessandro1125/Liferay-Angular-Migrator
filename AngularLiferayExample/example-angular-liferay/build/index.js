"use strict";

Liferay.Loader.define("example-angular-liferay@0.0.0/index", ['module', 'exports', 'require', './polyfills', '@example-angular-liferay$angular/platform-browser-dynamic', './app/app.component', './app/app.module', './app/dynamic.loader'], function (module, exports, require) {
    var define = undefined;
    Object.defineProperty(exports, "__esModule", { value: true });
    require("./polyfills");
    var platform_browser_dynamic_1 = require("@example-angular-liferay$angular/platform-browser-dynamic");
    var app_component_1 = require("./app/app.component");
    var app_module_1 = require("./app/app.module");
    var dynamic_loader_1 = require("./app/dynamic.loader");
    /**
     * This is the actual method that initializes the portlet. It is invoked by the
     * "bootstrap" module.
     *
     * @param  {LiferayParams} params an object with values of interest to the
     * 									portlet
     */
    function default_1(params) {
        platform_browser_dynamic_1.platformBrowserDynamic().bootstrapModule(app_module_1.AppModule).then(function (injector) {
            // Load the bootstrap component dinamically so that we can attach it
            // to the portlet's DOM, which is different for each portlet
            // instance and, thus, cannot be determined until the page is
            // rendered (during runtime).
            var dynamicLoader = new dynamic_loader_1.DynamicLoader(injector);
            dynamicLoader.loadComponent(app_component_1.AppComponent, params);
        });
    }
    exports.default = default_1;
    //# sourceMappingURL=index.js.map
});
//# sourceMappingURL=index.js.map