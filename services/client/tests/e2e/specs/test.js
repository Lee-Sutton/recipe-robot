describe('App layout specs', () => {
    beforeEach(() => {
        cy.visit('http://localhost:8080');
    });

    it('Should welcome the user', () => {
        cy.contains('h1', 'Welcome');
    });
});
