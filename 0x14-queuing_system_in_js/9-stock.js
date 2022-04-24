import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

function getItemById(id) {
  const idNum = Number(id);
  const product = listProducts.find((obj) => obj.id === idNum);
  return product;
}

function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const getAsync = promisify(client.get).bind(client);
  const res = await getAsync(`item.${itemId}`);
  return res;
}

const app = express();
const port = 1245;

app.get('/list_products', (req, res) => {
  const allProducts = listProducts.map((obj) => {
    return {
      itemId: obj.id,
      itemName: obj.name,
      price: obj.price,
      initialAvailableQuantity: obj.stock,
    };
  });

  res.json(allProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  try {
    const itemId = req.params.itemId;
    const curretnRes = await getCurrentReservedStockById(itemId);
    if (curretnRes === null) {
      return res.json({ status: 'Product not found' });
    }
    const obj = getItemById(itemId);
    res.json({
      itemId: obj.id,
      itemName: obj.name,
      price: obj.price,
      initialAvailableQuantity: obj.stock,
      currentQuantity: curretnRes,
    });
  } catch (error) {
    console.log(error);
  }
});

app.get('/reserve_product/:itemId', (req, res) => {
  const itemId = req.params.itemId;
  const obj = getItemById(itemId);
  if (obj === undefined) return res.json({ status: 'Product not found' });
  const curretnRes = obj.stock;
  if (curretnRes <= 0) {
    return res.json({ status: 'Not enough stock available', itemId: itemId });
  }

  reserveStockById(itemId, obj.stock);
  res.json({ status: 'Reservation confirmed', itemId: obj.id });
});

app.listen(port);
