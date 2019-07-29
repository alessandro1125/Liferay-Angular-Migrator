"use strict";

Liferay.Loader.define("example-angular-liferay@0.0.0/app/app-routing.module", ['module', 'exports', 'require', '@example-angular-liferay$angular/core', '@example-angular-liferay$angular/router', './test1/test1.component', './test2/test2.component', './test3/test3.component'], function (module, exports, require) {
    var define = undefined;
    var __decorate = this && this.__decorate || function (decorators, target, key, desc) {
        var c = arguments.length,
            r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc,
            d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    Object.defineProperty(exports, "__esModule", { value: true });
    var core_1 = require("@example-angular-liferay$angular/core");
    var router_1 = require("@example-angular-liferay$angular/router");
    var test1_component_1 = require("./test1/test1.component");
    var test2_component_1 = require("./test2/test2.component");
    var test3_component_1 = require("./test3/test3.component");
    var routes = [{ path: '', redirectTo: '/test1', pathMatch: 'full' }, { path: 'test1', component: test1_component_1.Test1Component }, { path: 'test2', component: test2_component_1.Test2Component }, { path: 'test3', component: test3_component_1.Test3Component }, { path: '**', redirectTo: '/test1' }];
    var AppRoutingModule = /** @class */function () {
        function AppRoutingModule() {}
        AppRoutingModule = __decorate([core_1.NgModule({
            imports: [router_1.RouterModule.forRoot(routes, { useHash: true, enableTracing: false })],
            exports: [router_1.RouterModule]
        })], AppRoutingModule);
        return AppRoutingModule;
    }();
    exports.AppRoutingModule = AppRoutingModule;
    //# sourceMappingURL=app-routing.module.js.map
});
//# sourceMappingURL=app-routing.module.js.map