// https://docs.cypress.io/api/introduction/api.html

describe('My First Test', () => {
  beforeEach(() => {
    cy.visit('http://localhost:8080');
  });

  it('Should welcome the user', () => {
    cy.contains('h1', 'Welcome to recipe robot!');
    cy.contains('About').click();
    cy.contains('h1', 'This is an about page').should('be.visible');
  });
});
