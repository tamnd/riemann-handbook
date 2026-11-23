---
id: flat-degree-holds
title: The degree of a flat frame section, restated
kind: theorem
decl: GlobalTheory.T.FlatDegree_holds
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.FlatDegreeHoldsStatement
covers: 685
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [`Fl.flatDegree`](/entry/flat-degree/), which has the content. It is a step toward [`topCovolSlim2_use_alt_alt`](/proof/literature/). It has two users. `goodTower_and_volume` passes it to [`exists_geometric_height_constants`](/entry/exists-geometric-height-constants/) and again to `volume_theorem_of_inputs`. `Br.degree_of_flatOnModel` passes it to `TopLL.degree_frames`.

## Statement

**Theorem.** `Fl.FlatDegree` holds.

Let $E$ be a CM field with a host $H$, and let $\chi$ be a Kronecker character modulo $H.d$. Let $\varphi$ be a frame function on a family of signature $(p, q)$ with a type, and let $N$ be a family of log norms of $\varphi$ at the infinite and finite places of the coefficient field. Suppose $\varphi$ is a flat generator on $U$ and $N$ is its family of norms. Then $N$ has finitely many nonzero finite entries, and
$$\deg N = \frac{p - q}{2}\,\operatorname{Re} \log\Omega_E(\chi) + q\bigl(2 \log \sqrt{d} - \log \operatorname{rd}(E)\bigr),$$
with $\log\Omega_E(\chi) = \gamma + \log\frac{2\pi}{\operatorname{rd}(E)} - \frac{L'}{L}(1, \chi)$.

## Proof

The statement is the same as that of `Fl.flatDegree`, and the proof applies it.

## In the Lean code

The theorem is in [FlatDegreeHoldsStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/FlatDegreeHoldsStatement.lean#L5). The proof is the pattern `first | exact @GlobalTheory.CompanionTheory.Ar.Fl.flatDegree | …`. The proposition `FlatDegree` is in [FlatDegree.lean](lean:Development/AutomorphicSpectrum/Statements/GeometryStatements/FlatDegree.lean#L12). The definition of `deg` uses a `finsum` over the finite places, which is $0$ when the support is infinite. So the first conclusion is needed to make the formula mean what it says.
