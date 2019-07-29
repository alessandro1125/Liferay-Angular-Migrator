"use strict";

Liferay.Loader.define("example-angular-liferay@0.0.0/app/app.component", ['module', 'exports', 'require', '@example-angular-liferay$angular/core'], function (module, exports, require) {
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
    var AppComponent = /** @class */function () {
        function AppComponent() {
            this.title = 'app';
        }
        AppComponent = __decorate([core_1.Component({
            selector: 'app-root',
            templateUrl: '/o/example-angular-liferay/app/app.component.html'
        })], AppComponent);
        return AppComponent;
    }();
    exports.AppComponent = AppComponent;
    //# sourceMappingURL=app.component.js.map
});
//# sourceMappingURL=app.component.js.map