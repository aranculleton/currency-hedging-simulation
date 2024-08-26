# Currency Hedging Simulation

## Project Overview

This project uses Python to model currency movements, hedging costs, and their impact on a hypothetical portfolio, with data collected from the [public API](https://www.alphavantage.co) offered by Alpha Vantage.

## Project Structure

- **data/**: Contains all the data used in this project.
  - **raw_fx_data/**: Raw foreign exchange rate data for multiple currency pairs.
  - **processed_data/**: Cleaned and processed foreign exchange data.
  - **macro_data/**: Macroeconomic data being used (CPI and unemployment)
  - **portfolio_data.csv**: Simulated portfolio data.
- **notebooks/**: Jupyter Notebook containing the full analysis and visualizations.
- **scripts/**: Python scripts used for data collection, processing, simulation, and analysis.
- **results/**: Output results from the simulations and visualizations.
- **requirements.txt**: Python dependencies needed to run the project.

## Getting Started

### Prerequisites

To run this project, you'll need Python 3.x installed on your system and the libraries included in the requirements file:

```bash
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any inquiries or support, feel free to open an issue or contact me at aran.culleton@proton.me.

---

**Note**: This project is intended for educational and demonstrative purposes and is not affiliated with or endorsed by BlackRock or its Aladdin platform.
