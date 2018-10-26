describe('App layout specs', () => {
    beforeEach(() => {
        cy.visit('http://localhost:8080');
    });

    it('Should welcome the user', () => {
        // The user navigates to the website and is welcomed
        cy.contains('h1', 'Welcome');

        // They see a link to create an account and they click it
        cy.contains('Create an account').click();

        // They fill in their account information
        cy.get('#email').clear().type('leesutton1@gmail.com');
        cy.get('#password').clear().type('password');
        cy.get('#password-confirm').clear().type('password');
        cy.get('[data-cy=create-account]').click();
    });
});
