const route = require('express').Router();
const TransactionService = require('../../services/transaction');

route.get('/', TransactionService.list);

route.get('/:id', TransactionService.get);

route.post('/', TransactionService.create);

route.patch('/:id', TransactionService.update);

route.delete('/:id', TransactionService.delete);

module.exports = route;