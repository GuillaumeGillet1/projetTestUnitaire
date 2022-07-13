describe('remplissage valeur', () => {
  it('Validation de la page', () => {
    cy.visit('localhost:8501/')
    cy.get('input').eq(0).clear().type('27').type('{enter}')
    cy.get('input').eq(1).clear().type('1').type('{enter}')
    cy.get('input').eq(2).clear().type('0').type('{enter}')
    cy.get('p').then((valeur) => {
      var val = parseFloat(valeur[0].innerText.substr(27))
      expect(val).to.be.greaterThan(10000)
    })
  })
})