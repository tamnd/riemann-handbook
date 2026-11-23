---
title: Automorphy implies the core properties
decls:
  - UpperTheory.V.Pa.pFromAut
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Automorphy implies the core properties

This section states the main theorem of the chapter for the universal ordinary determinant ring of a CM field. Its only input from automorphic forms is a Taylor-Wiles system at each family of Taylor-Wiles places. Its conclusions are two properties of an ideal $J$: it lies in every prime below a nice point of type I, and in every stable or thick prime below the end of a chain of nice points of type E. The proof assembles the results of the earlier sections. The theorem feeds the [vanishing step](/entry/vwin-of-hypotheses-h-e-alt/) of the modularity chapter. For the background see [automorphy lifting for unitary groups](/learn/deformations-patching/#automorphy-lifting-for-unitary-groups) and [modularity lifting](/learn/galois-representations/#modularity-lifting).

Let $L$ be a CM field with maximal totally real subfield $L^+$, fix an ordinary Hida setting with a level $V_0$, a coefficient ring $\mathcal{O}$, a residual datum $r$ of rank $n > 0$, and the universal ordinary determinant ring $B$ of $r$. For a point $x$ of $r$, the conditions are:

- $\mathrm{N}_1$: at each place $v$ the characters $\psi_{v,i}$ are distinct, and $\psi_{v,i} \ne \psi_{v,j} \cdot (\varepsilon \circ \phi_v)$ for $i < j$;
- *type I*: $\rho$ is absolutely irreducible on $G'$;
- *type E*: $\rho$ is conjugate to a block diagonal sum of two representations, of sizes $a, b \ge 1$, each with a form and absolutely irreducible on $G'$, with no nonzero $G'$-map between them;
- $\mathrm{N}_3$ and $\mathrm{N}_4$ as in the earlier sections.

A point $x$ *lies on* $B$ through $f$ if $f \colon B \to A$ is an $\mathcal{O}$-algebra map under which the universal determinant and the universal ordinary characters go to those of $\rho$.

The point is *nice of type I* if it satisfies $\mathrm{N}_1$, type I, $\mathrm{N}_3$ and $\mathrm{N}_4$, and *nice of type E* in the same way. A prime $q$ of $B$ is *stable* if over an algebraic closure of its residue field $D$ is the determinant of an absolutely irreducible representation. It is *thick* if it is not stable and the reduction at $q$ of the kernel algebra of $B$ is not semisimple.

The universal ring has *automorphy for $J$* if every Taylor-Wiles group with Taylor-Wiles places carries a Taylor-Wiles system for $J$ with no extra variable and $n[L^+ : \mathbb{Q}]$ weight variables.

**Theorem 7.13.1 (Automorphy implies the core properties).** Assume the published inputs of Galois cohomology. Assume that the level $V_0$ has the set of places of the setting, that local class field theory holds, that $\varepsilon \not\equiv 1 \bmod l$ on $\Gamma_0$, and that $B$ has automorphy for $J$. Then:

1. for every nice point $x$ of type I lying on $B$ through $f$, with $J \subseteq \ker f$, every prime $q \subseteq \ker f$ contains $J$;
2. for nice points $x_0, \dots, x_h$ of type E lying on $B$ through $f_0, \dots, f_h$, thick primes $e_i \subseteq \ker f_i \cap \ker f_{i+1}$, and a stable prime $q_1$ with $J \subseteq q_1 \subseteq \ker f_0$, every prime $q \subseteq \ker f_h$ that is stable or thick contains $J$.

Lean: `UpperTheory.V.Pa.pFromAut`.

*Proof.* Let $x_0, \dots, x_h$ be nice points. Each extends, after a finite extension of its ring, to a point of a frame with the inertia of the setting that satisfies $\mathrm{N}_3$ and $\mathrm{N}_4$, with $a = n$ in type I. The theorem on the choice of auxiliary elements gives $\sigma_1, \dots, \sigma_q$, extensions with one residue field size, bases of odd classes and split eigenvalues. The published inputs give the $\Phi$ condition and a Taylor-Wiles group with Taylor-Wiles places and these $\sigma_j$. Automorphy gives a Taylor-Wiles system with $n[L^+ : \mathbb{Q}]$ weight variables. The arithmetic first order bound and the arithmetic obstruction bound give $\mathrm{B}_1(n[L^+ : \mathbb{Q}] + nq)$ and $\mathrm{B}_2$, so each extended point is a point at level $n[L^+ : \mathbb{Q}] + nq$. The core patching theorem in general gives the chain conclusion.

For item 2, a stable prime is one where $D$ is discretely stable, and a thick prime is non-semisimple. Apply the chain conclusion. For item 1, take $h = 0$ and no $e_i$. At a nice point of type I, $D$ is discretely stable at every prime $q \subseteq \ker f$. So $q_1 = \ker f$ is stable with $J \subseteq q_1$, and every $q \subseteq \ker f$ is stable. $\square$

**Remark 7.13.2 (Formalization).** The statement `PfromAut` and the hypothesis `HasAut` are in [TaylorWilesObstructionBound.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PatchingModules/TaylorWilesObstructionBound.lean#L147), and the two conclusions `P1core` and `P3core` in [UniversalOrdinaryDeterminantRing.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/WeilGroupCharacters/UniversalOrdinaryDeterminantRing.lean#L284). `pFromAut` in [PfromAut.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PatchingModules/AutomorphicDetection/PfromAut.lean#L9) only applies `pFromAut_of` from [PFromAutOf.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PatchingModules/ChebotarevFamilies/PFromAutOf.lean#L116) to `norm`, `choice`, `arPl`, `b1Ar`, `b2Ar` and `raw`. The extension of the points is `norm`, the published construction of the Taylor-Wiles group is `arPl`, and the chain argument is the lemma `chain_of`. The passage from stable and thick primes to discretely stable and non-semisimple primes uses `Det.stableIff` and `Det.thickNonSS`, and the type I step uses `Det.typeIDisc`; we have not unfolded these three lemmas.

## Notes and references

The chapter feeds the modularity chapter. The core properties feed the [vanishing step](/entry/vwin-of-hypotheses-h-e-alt/), together with the presentation at an ordinary point. The stability theorem for $K$-theory feeds [Lemma K](/entry/lemma-k-lit-n-alt/), and the rank bound for odd homology feeds [the odd homology bound](/entry/b-odd/). The weighted presentations in rank three give the [count in case V](/entry/count-v-of-finiteness-duality-euler-host/). The cusp geometry results feed [the relation lemma](/entry/rel-onto/) and [the published hypotheses](/entry/published-hypotheses-from-patching-alt/).

Patching goes back to Taylor and Wiles [5], and Kisin [6] refined it. The deformation theory of representations attached to unitary groups is in Clozel, Harris and Taylor [7, §2]. Determinants and generalized matrix algebras are from Chenevier [9]. The Euler characteristic count in the Selmer bounds is the formula of Greenberg and Wiles [8, Theorem 2.19]. The stability results for $K$-theory and homology rest on Borel [1], van der Kallen [3] and Quillen [4], and the regularization of the cusp sections uses Borel [2]. The results here differ from the classical ones in form. The patching theorem is stated for chains of points and an abstract ideal $J$, not as an equality $R = T$, and the Selmer bounds are stated over power series rings $K[[t]]$ with explicit constants.

1. A. Borel, "Stable real cohomology of arithmetic groups", *Ann. Sci. École Norm. Sup.* (4) 7 (1974), 235 to 272.
2. A. Borel, "Regularization theorems in Lie algebra cohomology. Applications", *Duke Math. J.* 50 (1983), 605 to 623.
3. W. van der Kallen, "Homology stability for linear groups", *Invent. Math.* 60 (1980), 269 to 295.
4. D. Quillen, "Higher algebraic K-theory: I", *Lecture Notes in Math.* 341 (1973), 85 to 147.
5. R. Taylor and A. Wiles, "Ring-theoretic properties of certain Hecke algebras", *Ann. of Math.* 141 (1995), 553 to 572.
6. M. Kisin, "Moduli of finite flat group schemes, and modularity", *Ann. of Math.* 170 (2009), 1085 to 1180.
7. L. Clozel, M. Harris and R. Taylor, "Automorphy for some l-adic lifts of automorphic mod l Galois representations", *Publ. Math. IHÉS* 108 (2008), 1 to 181, §2.
8. H. Darmon, F. Diamond and R. Taylor, "Fermat's Last Theorem", Theorem 2.19 (the formula of Greenberg and Wiles).
9. G. Chenevier, "The p-adic analytic space of pseudocharacters of a profinite group and pseudorepresentations over arbitrary rings", *LMS Lecture Note Ser.* 414 (2014), 221 to 285.
