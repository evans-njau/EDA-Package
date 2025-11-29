### `top_n(items, n)`
Returns the top **n** highest elements from a list or array.

**Arguments:**
- **items (array/list):** A list of numeric items.
- **n (int):** Number of items to return.

**Returns:**
- **array:** The top `n` items sorted in **descending** order.

**Example:**
```python
from eda_package import top_n

top_n([1, 7, 8, 9, 0, 6], 3)
# Output: [9, 8, 7]
```bash
pip install git+https://github.com/evans-njau/EDA-Package.git
