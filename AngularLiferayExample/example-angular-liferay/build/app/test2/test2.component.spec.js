"use strict";

Liferay.Loader.define("example-angular-liferay@0.0.0/app/test2/test2.component.spec", ['module', 'exports', 'require', '@example-angular-liferay$angular/core/testing', './test2.component'], function (module, exports, require) {
    var define = undefined;
    Object.defineProperty(exports, "__esModule", { value: true });
    var testing_1 = require("@example-angular-liferay$angular/core/testing");
    var test2_component_1 = require("./test2.component");
    describe('Test2Component', function () {
        var component;
        var fixture;
        beforeEach(testing_1.async(function () {
            testing_1.TestBed.configureTestingModule({
                declarations: [test2_component_1.Test2Component]
            }).compileComponents();
        }));
        beforeEach(function () {
            fixture = testing_1.TestBed.createComponent(test2_component_1.Test2Component);
            component = fixture.componentInstance;
            fixture.detectChanges();
        });
        it('should create', function () {
            expect(component).toBeTruthy();
        });
    });
    //# sourceMappingURL=test2.component.spec.js.map
});
//# sourceMappingURL=test2.component.spec.js.map