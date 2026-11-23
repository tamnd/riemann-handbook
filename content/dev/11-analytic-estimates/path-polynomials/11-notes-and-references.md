---
title: Notes and references
decls:
  - Formalism.MainNotions.G.SymmetricFormBlocks.orthLat_of'
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Notes and references

The chapter feeds three results. The closed form of Theorem A, reduced in Sections 6 to 8 to the window condition and two facts about lattices, is used in [the closed form of Theorem A](/entry/theorem-a-closed-form-holds/). The operator at one tie of Section 5 is the core of [the theorem on the tie operators](/entry/tie-ops-x-main/), and the leading term and the monotonicity of Section 2 are used in [the theorem on the mean of the ratios](/entry/mean-gam-x/). The splitting package of Section 9 goes into [the tool statements](/entry/tool-statements-hold/), the bracket polynomial span into [the bracket lemma](/entry/b10/), and the admissible words and the column and pre-systems of Section 10 into the step [theta local matching](/step/theta-local-matching/).

Section 1 is the theory of Jordan splittings of lattices over $\mathbb{Z}_p$ for odd $p$, with the pairing linear in one variable and symmetric on the lattice. Classically one proves that a lattice over a non-dyadic local ring has an orthogonal basis, by splitting off a vector of minimal valuation; this is the minimal vector step of Section 1, and the classical source is O'Meara, §91 and §92. The Lean statements count good vectors at a depth instead of stating the splitting, because Sections 6 to 8 need the number of basis vectors whose valuation is below the depth, and they keep $p \neq 2$ as a hypothesis, which the window hypotheses supply. See [lattices over Dedekind domains](/learn/hermitian-lattices/#lattices-over-dedekind-domains) and [lattices in quadratic and hermitian spaces](/learn/hermitian-lattices/#lattices-in-quadratic-and-hermitian-spaces).

The Fock pairing of Section 2 is the Fischer pairing, for which differentiation is adjoint to multiplication; it is the pairing of the [Fock model](/learn/theta/#the-fock-model), and its use for the invariant theory of several vector and covector letters goes back to Howe. The tie operators, the leading term and the box bound of Section 6 have no classical counterpart that we know of.

The path polynomials of Section 9 are a basis adapted to the branching of mixed tensor products of symmetric powers. For vector letters alone, a path is a sequence of partitions that grows by horizontal strips, which is Pieri's rule (Macdonald, Chapter I, §5), and the path polynomials are products of column determinants as in the construction of the Schur modules by minors (Fulton, Chapter 8). Words with covector letters correspond to the rational tableaux of Stembridge. The theorem on admissible words is stated over a field only, and the conditions A3 over a discrete valuation ring and its residue field only; the Lean form does not claim A3 over other rings. The bracket polynomials of Section 9 are the bideterminants of De Concini, Eisenbud and Procesi, and the Theorem (Bracket polynomial span) is the statement that the standard bideterminants span the integral form of the induced module, the dual of the Weyl module for the Kostant $\mathbb{Z}$-form. The Lean form states it inside the rational polynomials, with the integral form described by the condition $\nabla$ on the highest weight component (see Green, Chapter 4, and Jantzen, Part II, Chapter 2). See also [Schur polynomials](/learn/combinatorics/#schur-polynomials), [the Pieri and Littlewood-Richardson rules](/learn/combinatorics/#the-pieri-and-littlewood-richardson-rules) and [highest weights](/learn/representations/#highest-weights-and-branching).

The column systems and pre-systems of Section 10 are bookkeeping for the local matching: they record, column by column, a lift of each factor with its order, so that the orders and the degrees of the full product can be added. The only combinatorial input is that a horizontal strip has at most one box in each column (Macdonald, Chapter I, §1).

- J. A. Green, *Polynomial Representations of $\mathrm{GL}_n$*, Lecture Notes in Math. 830, Springer, 1980, Chapter 4.
- C. De Concini, D. Eisenbud and C. Procesi, Young diagrams and determinantal varieties, Invent. Math. 56 (1980), 129 to 165, §1.
- W. Fulton, *Young Tableaux*, London Math. Soc. Student Texts 35, Cambridge University Press, 1997, Chapter 8.
- R. Howe, Remarks on classical invariant theory, Trans. Amer. Math. Soc. 313 (1989), 539 to 570.
- J. C. Jantzen, *Representations of Algebraic Groups*, 2nd ed., Math. Surveys Monogr. 107, Amer. Math. Soc., 2003, Part II, Chapter 2.
- B. Kostant, Groups over $\mathbb{Z}$, in *Algebraic Groups and Discontinuous Subgroups*, Proc. Sympos. Pure Math. 9, Amer. Math. Soc., 1966, 90 to 98.
- I. G. Macdonald, *Symmetric Functions and Hall Polynomials*, 2nd ed., Oxford University Press, 1995, Chapter I, §1 and §5.
- O. T. O'Meara, *Introduction to Quadratic Forms*, Grundlehren 117, Springer, 1963, Chapter IX, §91 and §92.
- J. R. Stembridge, Rational tableaux and the tensor algebra of $\mathfrak{gl}_n$, J. Combin. Theory Ser. A 46 (1987), 79 to 120.

**Remark 7.11.1 (Formalization).** The decl listed for this section, `orthLat_of'`, is the Lean form of the orthogonal family theorem of Section 1, which the classical sources above state as the existence of an orthogonal basis.
