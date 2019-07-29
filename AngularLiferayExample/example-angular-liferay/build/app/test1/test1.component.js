"use strict";

Liferay.Loader.define("example-angular-liferay@0.0.0/app/test1/test1.component", ['module', 'exports', 'require', '@example-angular-liferay$angular/core'], function (module, exports, require) {
    var define = undefined;
    var __decorate = this && this.__decorate || function (decorators, target, key, desc) {
        var c = arguments.length,
            r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc,
            d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __metadata = this && this.__metadata || function (k, v) {
        if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
    };
    Object.defineProperty(exports, "__esModule", { value: true });
    var core_1 = require("@example-angular-liferay$angular/core");
    var Test1Component = /** @class */function () {
        function Test1Component() {}
        Test1Component.prototype.ngOnInit = function () {};
        Test1Component = __decorate([core_1.Component({
            selector: 'app-test1',
            templateUrl: '/o/example-angular-liferay/app/test1/test1.component.html'
        }), __metadata("design:paramtypes", [])], Test1Component);
        return Test1Component;
    }();
    exports.Test1Component = Test1Component;
    //# sourceMappingURL=test1.component.js.map
});
//# sourceMappingURL=test1.component.js.map