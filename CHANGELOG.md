# Changelog

## Unreleased

## v0.1.9

- Volume 3, schemes and étale cohomology: all ten chapters are written. The last is *Vanishing*: Tate's Euler characteristic formula, Poitou-Tate duality with normalised invariants, the Jacquet-Shalika bound, the pole of the Rankin-Selberg L-function, and the de Rham property of Hecke characters. The volume has 351 pages.
- Volume 4, p-adic Hodge theory: two new chapters, *Hodge-Tate periods* and *Prismatic Dieudonné theory*, with crystalline cohomology from smooth lifts. The volume has 223 pages.
- Volume 10, Hermitian lattices: the chapter on Hermitian genera is complete, in 10 sections. The volume has 186 pages.
- The pull requests list what the writers found in the Lean code.

## v0.1.8

- The development volumes are now Volumes 3 to 15, grouped by subject: 104 chapters with all 5,756 planned entries. The old volumes followed the branches and folders of the Lean code. The design is in ledger/structure.yaml, and `rhb ledger` builds the outline from it. The entry ids are the same, so links to entries keep working.
- The written chapters moved with their entries. The two chapters on cup products and Kummer classes are now one chapter of Volume 3, *The Kummer sequence, cup products and Chern classes*.
- A chapter can mix written sections and entries: the sections come first, then the entries.
- The old volume introductions are gone, since their volumes are gone. The new volumes have no introduction yet.
- Chapters written as mathematics, in the style of Volume 1: numbered definitions and theorems, proofs, a `Lean:` line under each result, and notes and references. Each chapter replaces its older entries.
- Volume 3, schemes and étale cohomology: nine of ten chapters are written. These are Künneth formulas, purity, proper base change, the Kummer sequence and Chern classes, finite étale covers, Kummer classes and Picard torsion, formal algebraization, resolution of singularities, and L2 methods. The volume has 329 pages.
- Volume 4, p-adic Hodge theory: period rings, the comparison theorems, and Breuil-Kisin modules.
- Volume 10, Hermitian lattices: class numbers and the first part of Hermitian genera.
- Volume 12, the theta correspondence: theta-Parseval.
- `rhb number --write` writes the statement numbers and the numbers of links into the chapter sources.
- The riemann pin moves to the Volume 1 with 29 chapters.
- The pull requests list what the writers found in the Lean code.

## v0.1.7

- Tier 2 is complete: every declaration that owns 300 or more others has an entry. Vols 3 to 12 have all their planned entries.
- Volume 7, the unitary hypotheses: 565 entries in 28 chapters. The introduction names the small chapters.
- Volume 8, automorphic arithmetic: 75 entries in 4 chapters.
- Volume 9, abelian varieties: 406 entries in 12 chapters.
- Volume 10, the Weil bound, the spectrum and resolution: 134 entries in 16 chapters. New chapters cover the twisted trace formula, the classical vanishing theorems, Bernstein's irreducibility theorem and the local converse theorem for GL(n).
- Volume 11, the formalism: 101 entries in 15 chapters, with the Hermitian mass formula in a new chapter.
- Volume 12, the ground theory: 38 entries in 14 chapters, with local reciprocity, Poitou-Tate duality with real places, Hörmander's estimate and the finiteness of coherent cohomology.
- One Volume 9 entry now says correctly where the content of `frobenius_lifting` is.
- Volumes 7 to 12 build with no overfull lines and no unresolved links.
- The pull requests for each volume list what the writers found in the Lean code. Two reports say that one name may be declared twice in files that are imported together, and these need a check with a full build.

## v0.1.6

- Volume 5, volume estimates and positivity: the 181 tier 2 entries. Twelve chapters have new titles, and the introduction lists all 13 chapters.
- Volume 6, theta integrals: the tier 2 entries. Six chapters have new titles, and the introduction lists all 10 chapters.
- Two wide displays in Volume 5 are split over two lines, so the volume builds with no overfull lines.
- One statement in Volume 5 now uses the rank of the submodule, as the Lean code does.
- The pull requests for Volumes 5 and 6 list what the writers found in the Lean code.

## v0.1.5

- The outline now plans tier 2: every declaration that owns 300 or more others gets an entry. 54 entries moved to their tier 2 chapters.
- Volume 3, the Galois row: the 145 tier 2 entries, so all 209 planned entries are written. Two chapters have new titles, and the introduction lists the new chapters.
- Volume 4, the window bound: the 84 tier 2 entries, so all 146 planned entries are written. Six chapters have new titles that say what is in them.
- A link to an entry that a proof chapter covers now goes to that chapter or to the step.
- The pull requests for Volumes 3 and 4 list what the writers found in the Lean code: unused hypotheses, duplicate theorems and names that do not match their statements.
- Volumes 3 and 4 build with no overfull lines and no unresolved links.

## v0.1.4

- Volume 8, automorphic arithmetic: all 36 tier 1 entries and an introduction.
- Volume 9, abelian varieties: all 69 tier 1 entries and an introduction. The entries cover toroidal compactifications, the arithmetic Hilbert-Samuel formula, pseudo-coefficients, the Jacquet-Rallis fundamental lemma and p-adic monodromy.
- Volume 10, resolution, Siegel-Weil and GL: all 24 tier 1 entries and an introduction. The code proves strong resolution of singularities in characteristic 0 with no hypothesis.
- Volume 11, the formalism: all 35 tier 1 entries and an introduction, with the chain of 20 reductions below Theorem A.
- Volume 12, the ground theory: all 6 tier 1 entries and an introduction.
- Two chapter titles are fixed: "Siegel-Weil" and "Representation theory of GL".
- All 13 volumes build with no overfull lines and no unresolved links.
- The tier 1 plan is complete: 591 of 591 entries are written.

## v0.1.3

- Volume 6, theta integrals and the green window: all 25 tier 1 entries and an introduction. The entries cover the two theta statements from the Siegel-Weil formula, and the short branch that ends in the nonvanishing of L(s, ψ) for Re(s) > 1/2.
- Volume 7, the unitary hypotheses: all 220 tier 1 entries and an introduction, in 17 chapters. Volume 7 is 250 pages. The entries cover the three branches below the last node of the trunk: the record HypsAlt from rows, the map onto X with the lower bound for λ, and the twelve open parameter statements.
- Five entries now link the generic row statement of the Lean code, not the Galois row of Volume 2.
- Volumes 0 to 7 build with no overfull lines.
- The ledger now shows 426 of the 591 tier 1 entries written.

## v0.1.2

- Volume 4, the window bound: all 52 tier 1 entries and an introduction. The entries cover the modularity argument for the cases I to Z, the Iwahori reduction and the Euler system of zeta classes.
- Volume 5, volume estimates and positivity: all 43 tier 1 entries and an introduction. The entries cover the covolume bound, the good tower and the volume theorem, and the Siegel lemma.
- One wide formula in Volume 4 is split. Volumes 0 to 5 build with no overfull lines.
- The ledger now shows 189 of the 591 tier 1 entries written.

## v0.1.1

- Volume 3, the Galois row: all 62 tier 1 entries, 54 of them new, and an introduction. Volume 3 is 73 pages.
- The entries record what is odd in the Lean code: names that say something other than the statement, hypotheses that are never used, and definitions by choice that default to 0.
- Typesetting: wide tables wrap, bare module paths and long lines of code break, and three wide formulas in tamnd/riemann are split. Volumes 0 to 3 build with no overfull lines.
- Pinned to tamnd/riemann d5aa0616 and tamnd/riemann-lean af705e0d.

## v0.1.0

- The builder `rhb`: the Learn pages and the written proof of tamnd/riemann as Volumes 1 and 2, the front pages as Volume 0, and the entries of `content/dev/` as Volumes 3 and later, in PDF and EPUB.
- Numbered chapters, sections and statements (Definition 3.2.1), and references between volumes.
- The ledger: an entry for each declaration with a dominated subtree of 1,000 or more declarations, assigned to volumes and chapters.
- The brief for the writers of entries.
