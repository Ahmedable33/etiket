const PRODUCTS = [
    { category: "Fruits", price: "$1", stocked: true, name: "Apple" },
    { category: "Fruits", price: "$1", stocked: true, name: "Dragonfruit" },
    { category: "Fruits", price: "$2", stocked: false, name: "Passionfruit" },
    { category: "Vegetables", price: "$2", stocked: true, name: "Spinach" },
    { category: "Vegetables", price: "$4", stocked: false, name: "Pumpkin" },
    { category: "Vegetables", price: "$1", stocked: true, name: "Peas" }
]

class FilterableProductTable extends React.Component
{
    constructor(props) {
        super(props);
        this.state = {
            filterText : '',
            inStockOnly : false
        }
        this.handleFilterTextChange = this.handleFilterTextChange.bind(this)
        this.handleInstockOnly = this.handleInstockOnly.bind(this)
    }

    handleFilterTextChange (filterText)
    {
        this.setState({filterText})
    }

    handleInstockOnly (inStockOnly)
    {
        this.setState({inStockOnly})
    }

    render()
    {
        const {products} = this.props
        return <div>
            <SearchBar
                filterText={this.state.filterText}
                instockOnly={this.state.inStockOnly}
                onFilterTextChange={this.handleFilterTextChange}
                onStockChange={this.handleInstockOnly}
            />
            <ProductTable
                filterText={this.state.filterText}
                inStockOnly={this.state.inStockOnly}
                products={products}/>
        </div>
    }
}

class SearchBar extends React.Component
{
    constructor(props) {
        super(props);
        this.state= {seach_product: '' , onshow: false}
        this.handleFilterTextChange = this.handleFilterTextChange.bind(this)
        this.handleinStockOnly = this.handleinStockOnly.bind(this)
    }

    handleFilterTextChange(e)
    {
        this.props.onFilterTextChange(e.target.value)
    }

    handleinStockOnly(e)
    {
        this.props.onStockChange(e.target.checked)
    }


    render()
    {
        const {filterText , inStockOnly} = this.props
        return <form>
            <input type='text' placeholder="search" value={filterText}  onChange={this.handleFilterTextChange}/> <br/>
            <input type="checkbox"  checked={inStockOnly}  onChange={this.handleinStockOnly} /> <label>Only show products in stock </label>
        </form>
    }
}

function ProductTable({products , inStockOnly , filterText})
{
    let row = []
    let last_category = null
    products.forEach(product => {
        if ((inStockOnly && !product.stocked) || product.name.indexOf(filterText) === -1 )
        {
            return
        }

        if (product.category !== last_category)
        {
            last_category = product.category
            row.push(<ProductCategoryRow category={product.category}/>)
        }
        row.push(<ProductRow product={product}/> )

    })

    return <table>
        <thead>
        <tr>
            <td>
                Name
            </td>
            <td>
                Price
            </td>
        </tr>
        </thead>
        <tbody>
        {row}

        </tbody>


    </table>
}

function ProductCategoryRow({category})
{
    return <th>
        {category}
    </th>
}

function ProductRow({product})
{
    return <tr>
        <td>
            {product.name}
        </td>
        <td>
            {product.price}
        </td>
    </tr>
}

ReactDOM.render(<FilterableProductTable products = {PRODUCTS}/> , document.getElementById('login-container') )