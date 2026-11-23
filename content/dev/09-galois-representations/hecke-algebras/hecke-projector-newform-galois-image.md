---
id: hecke-projector-newform-galois-image
title: The Hecke projector onto the Galois image of a newform (restatement)
kind: theorem
decl: GlobalTheory.T.heckeProjector_newform_galoisImage
module: Development.AbelianVarietyTheory.Proofs.FoundationProofs.HeckeProjectorNewformGaloisImageStatement
covers: 1162
status: drafted
drafted_by: writer@claude
---
This theorem gives, for a newform $g$ of odd weight $k \ge 3$ and an irreducible Galois representation $\rho$ with the Hecke eigenvalues of $g$, a Hecke operator that projects an $\ell$-adic space attached to a tower of modular function fields onto copies of $\rho$. [The admissible functional on the tower](/entry/kato-global-admissibility-of-admissible/) uses it as its main input. This is a renaming. The real content is in [the Hecke projector for a newform](/entry/hecke-proj-newform/).

## Statement

The statement is word for word the statement of `GlobalTheory.KZ.HeckeProj.heckeProj_newform`. In short: let $g$ be a newform of odd weight $k \ge 3$ and character $\chi$, let $\ell \ne 2$ be a prime, and let $N \ge 5$ be a multiple of the level of $g$ prime to $\ell$. Let $\alpha$ be a root of $X^2 - a_\ell(g) X + \chi(\ell)\ell^{k-1}$ with $\alpha^2 \ne \chi(\ell)\ell^{k-1}$ and $\alpha^2 \ne \chi(\ell)\ell^{k-2}$. Let $\rho \colon \mathrm{Gal}(\overline{\mathbb{Q}}/\mathbb{Q}) \to \mathrm{GL}_2(E)$ be irreducible, with the traces $a_q(g)$ (through an isomorphism $E \cong \mathbb{C}$) and determinants $q^{k-1}\chi(q)$ at Frobenius elements outside a finite set. Then there are Galois and Hecke equivariant maps $\pi_i$, $\sigma_i$ between this space and $E^2$, with $\pi_i \sigma_j = \delta_{ij}$, and a Hecke operator $P$ with eigenvalue $1$ that acts as $\sum_i \sigma_i \pi_i$. The full statement is in the entry for `heckeProj_newform`.

## Proof

The proof is

```
first | exact @GlobalTheory.KZ.HeckeProj.heckeProj_newform | ...
```

It applies `heckeProj_newform` to the same arguments.

## In the Lean code

The theorem is in [HeckeProjectorNewformGaloisImageStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/HeckeProjectorNewformGaloisImageStatement.lean#L9). It only copies the statement of `heckeProj_newform` into the namespace `GlobalTheory.T`. The size of its subtree, 1,162, is the size of that of `heckeProj_newform` plus one.
