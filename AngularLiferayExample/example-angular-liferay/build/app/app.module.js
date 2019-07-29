"use strict";

Liferay.Loader.define("example-angular-liferay@0.0.0/app/app.module", ['module', 'exports', 'require', '@example-angular-liferay$angular/platform-browser', '@example-angular-liferay$angular/core', '@example-angular-liferay$angular/common', './app-routing.module', './app.component', './test1/test1.component', './test2/test2.component', './test3/test3.component'], function (module, exports, require) {
    var define = undefined;
    var __decorate = this && this.__decorate || function (decorators, target, key, desc) {
        var c = arguments.length,
            r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc,
            d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    Object.defineProperty(exports, "__esModule", { value: true });
    var platform_browser_1 = require("@example-angular-liferay$angular/platform-browser");
    var core_1 = require("@example-angular-liferay$angular/core");
    var common_1 = require("@example-angular-liferay$angular/common");
    var app_routing_module_1 = require("./app-routing.module");
    var app_component_1 = require("./app.component");
    var test1_component_1 = require("./test1/test1.component");
    var test2_component_1 = require("./test2/test2.component");
    var test3_component_1 = require("./test3/test3.component");
    var AppModule = /** @class */function () {
        function AppModule() {}
        AppModule.prototype.ngDoBootstrap = function () {};
        AppModule = __decorate([core_1.NgModule({
            entryComponents: [app_component_1.AppComponent],
            declarations: [app_component_1.AppComponent, test1_component_1.Test1Component, test2_component_1.Test2Component, test3_component_1.Test3Component],
            imports: [platform_browser_1.BrowserModule, app_routing_module_1.AppRoutingModule],
            providers: [{ provide: common_1.APP_BASE_HREF, useValue: '/' }],
            bootstrap: []
        })], AppModule);
        return AppModule;
    }();
    exports.AppModule = AppModule;
    //# sourceMappingURL=app.module.js.map
});
//# sourceMappingURL=app.module.js.map