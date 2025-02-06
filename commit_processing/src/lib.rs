use std::path::PathBuf;

use pyo3::prelude::*;
use thiserror::Error;
mod parse;

pub type Result<'a, T> = std::result::Result<T, ParseDiffError>;

#[derive(Error, Debug)]
pub enum ParseDiffError {
    #[error("IO operation failed {0}")]
    IOError(#[from] std::io::Error),
    #[error("parsing of file {0} failed with")]
    ParseError(#[from] parse::ParseError<'static>),
}

#[pyclass]
#[derive(Default, Debug)]
struct PyDiff {}

#[pymodule]
fn parse_diff(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(parse_diff_file, m)?)
}
#[pyfunction]
fn parse_diff_file(diff: PathBuf) -> PyResult<Vec<PyDiff>> {
    Ok(Vec::default())
}

#[cfg(test)]
mod tests {
    use super::*;
}
