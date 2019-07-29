"use strict";

Liferay.Loader.define("example-angular-liferay@0.0.0/app/dynamic.loader", ['module', 'exports', 'require', '@example-angular-liferay$angular/core'], function (module, exports, require) {
    var define = undefined;
    Object.defineProperty(exports, "__esModule", { value: true });
    var core_1 = require("@example-angular-liferay$angular/core");
    /**
     * This class loads an Angular component dinamically so that we can attach it to
     * the portlet's DOM, which is different for each portlet instance and thus,
     * cannot be determined until the page is rendered (during runtime).
     */
    var DynamicLoader = /** @class */function () {
        function DynamicLoader(injector) {
            this.injector = injector;
        }
        DynamicLoader.prototype.loadComponent = function (component, params) {
            var _this = this;
            var node = document.getElementById(params.portletElementId);
            this.injector.get(core_1.NgZone).run(function () {
                var componentFactory = _this.injector.get(core_1.ComponentFactoryResolver).resolveComponentFactory(component);
                var componentRef = componentFactory.create(_this.injector, [], node);
                componentRef.instance.params = params;
                _this.injector.get(core_1.ApplicationRef).attachView(componentRef.hostView);
            });
        };
        return DynamicLoader;
    }();
    exports.DynamicLoader = DynamicLoader;
    //# sourceMappingURL=dynamic.loader.js.map
});
//# sourceMappingURL=dynamic.loader.js.map