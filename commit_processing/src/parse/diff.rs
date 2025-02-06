use std::path::Path;

/// diff of a file
#[derive(PartialEq, Eq, PartialOrd, Ord, Debug, Clone)]
pub struct Diff<'a> {
    path: &'a Path,
    code: Vec<Modified<'a>>,
}

/// a modified block
#[derive(Debug, PartialEq, Eq, PartialOrd, Ord, Clone)]
pub struct Modified<'a> {
    old: &'a str,
    new: &'a str,
}

impl<'a> Diff<'a> {
    pub fn new(p: &'a Path) -> Self {
        Self {
            path: p,
            code: Vec::new(),
        }
    }
}

impl<'a> Modified<'a> {
    fn new(old: &'a str, new: &'a str) -> Self {
        Self { old, new }
    }
}
