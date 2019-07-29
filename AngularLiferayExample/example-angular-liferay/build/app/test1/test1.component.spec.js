"use strict";

Liferay.Loader.define("example-angular-liferay@0.0.0/app/test1/test1.component.spec", ['module', 'exports', 'require', '@example-angular-liferay$angular/core/testing', './test1.component'], function (module, exports, require) {
    var define = undefined;
    Object.defineProperty(exports, "__esModule", { value: true });
    var testing_1 = require("@example-angular-liferay$angular/core/testing");
    var test1_component_1 = require("./test1.component");
    describe('Test1Component', function () {
        var component;
        var fixture;
        beforeEach(testing_1.async(function () {
            testing_1.TestBed.configureTestingModule({
                declarations: [test1_component_1.Test1Component]
            }).compileComponents();
        }));
        beforeEach(function () {
            fixture = testing_1.TestBed.createComponent(test1_component_1.Test1Component);
            component = fixture.componentInstance;
            fixture.detectChanges();
        });
        it('should create', function () {
            expect(component).toBeTruthy();
        });
    });
    //# sourceMappingURL=test1.component.spec.js.map
});
//# sourceMappingURL=test1.component.spec.js.map