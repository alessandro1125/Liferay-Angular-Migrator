"use strict";

Liferay.Loader.define("example-angular-liferay@0.0.0/app/test3/test3.component.spec", ['module', 'exports', 'require', '@example-angular-liferay$angular/core/testing', './test3.component'], function (module, exports, require) {
    var define = undefined;
    Object.defineProperty(exports, "__esModule", { value: true });
    var testing_1 = require("@example-angular-liferay$angular/core/testing");
    var test3_component_1 = require("./test3.component");
    describe('Test3Component', function () {
        var component;
        var fixture;
        beforeEach(testing_1.async(function () {
            testing_1.TestBed.configureTestingModule({
                declarations: [test3_component_1.Test3Component]
            }).compileComponents();
        }));
        beforeEach(function () {
            fixture = testing_1.TestBed.createComponent(test3_component_1.Test3Component);
            component = fixture.componentInstance;
            fixture.detectChanges();
        });
        it('should create', function () {
            expect(component).toBeTruthy();
        });
    });
    //# sourceMappingURL=test3.component.spec.js.map
});
//# sourceMappingURL=test3.component.spec.js.map