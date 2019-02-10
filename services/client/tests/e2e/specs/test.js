describe('App layout specs', () => {
    beforeEach(() => {
        cy.resetDb();
        cy.visit('/');
    });

    it('Should allow users to signup', () => {
        const user = {
            username: 'leeSutton',
            email: 'lee@e.com',
            password: '@password123',
        };
        // The user navigates to the website and is welcomed
        cy.contains('h1', 'Welcome');

        // They see a link to create an account and they click it
        cy.contains('Create an account').click();

        // They fill in their account information
        cy.get('[data-cy=username]').type(user.username);
        cy.get('[data-cy=email]').type(user.email);
        cy.get('[data-cy=password1]').type(user.password);
        cy.get('[data-cy=password2]').type(user.password);
        cy.get('form').submit();

        // The user is redirected to their home page
        // cy.contains(`Welcome ${user.username}`)
    });
});
