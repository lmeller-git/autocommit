use std::str::FromStr;

use super::{
    diff::{Diff, Modified},
    ParseError,
};

impl<'a> FromStr for Diff<'a> {
    type Err = ParseError<'a>;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        todo!()
    }
}

impl<'a> FromStr for Modified<'a> {
    type Err = ParseError<'a>;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        todo!()
    }
}
