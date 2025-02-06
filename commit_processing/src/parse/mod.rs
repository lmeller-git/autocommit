pub mod diff;
pub mod parse_diff;
use diff::Diff;
use thiserror::Error;

pub type Result<'a, T> = std::result::Result<T, ParseError<'a>>;

#[derive(Error, Debug)]
pub enum ParseError<'a> {
    #[error("cannot parse from {0}")]
    BadStr(&'a str),
}

pub fn parse_diff<'a>(diff: &'a str) -> Result<Vec<Diff<'a>>> {
    let mut diffs = Vec::new();
    for d in diff.split('@') {
        diffs.push(d.parse::<Diff>()?);
    }
    Ok(diffs)
}
