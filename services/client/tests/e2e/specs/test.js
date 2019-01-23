describe('App layout specs', () => {
    beforeEach(() => {
        cy.visit('/');
    });

    it('Should allow users to signup', () => {
        // The user navigates to the website and is welcomed
        cy.contains('h1', 'Welcome');

        // They see a link to create an account and they click it
        cy.contains('Create an account').click();

        // They fill in their account information
        cy.get('[data-cy=username]').type('leeSutton');
        cy.get('[data-cy=email]').type('leesutton1@gmail.com');
        cy.get('[data-cy=password1]').type('password');
        cy.get('[data-cy=password2]').type('password');
        cy.get('form').submit();
    });
});
