---
id: hecke-proj-newform
title: A Hecke projector onto copies of the Galois representation of a newform
kind: theorem
decl: GlobalTheory.KZ.HeckeProj.heckeProj_newform
module: Development.AbelianVarietyTheory.Proofs.FoundationProofs.HeckeProjectorNewformGaloisImage
covers: 1161
status: drafted
drafted_by: writer@claude
---
This theorem cuts out, inside an $\ell$-adic space attached to a tower of modular function fields, the part where the Hecke operators act by the eigenvalues of a newform $g$. It shows that this part is a sum of copies of a given Galois representation $\rho$ of $g$, and that a Hecke operator projects onto it. It is restated as [the Hecke projector onto the Galois image](/entry/hecke-projector-newform-galois-image/), which [the admissible functional on the tower](/entry/kato-global-admissibility-of-admissible/) uses.

## Statement

Let $\Omega$ be an algebraic closure of $\mathbb{Q}$ with an embedding $\varepsilon \colon \Omega \to \mathbb{C}$, and let $X$ be a tower of modular function fields over $\Omega$ (the Lean structure `Tower`) whose $j$-function is holomorphic on the upper half plane. For a prime $\ell$, let $\mathrm{Fn}_\ell$ be the functions on $\mathbb{Z}_\ell^2$ with values in the $\ell$-adic completion of $K^\times \otimes \mathbb{Z}_\ell$, where $K$ is the function field of $X$. The tower gives a Galois action and Hecke operators $T_q$, $U$ and diamond operators $\langle d \rangle$ on a subspace $V_B \subset E \otimes \mathrm{Fn}_\ell$.

Let $g$ be a newform of odd weight $k \ge 3$ with character $\chi$. Let $\ell \ne 2$ be a prime and $N \ge 5$ a multiple of the level of $g$ with $\gcd(N, \ell) = 1$. Let $\alpha$ be a root of $X^2 - a_\ell(g) X + \chi(\ell)\ell^{k-1}$ with $\alpha^2 \ne \chi(\ell)\ell^{k-1}$ and $\alpha^2 \ne \chi(\ell)\ell^{k-2}$. Let $\lambda$ be the eigensystem $T_q \mapsto a_q(g)$ for $q \nmid N\ell$, $U \mapsto \alpha$, $\langle d \rangle \mapsto \chi(d)$. Let $E$ be an algebraically closed normed field over $\mathbb{Z}_\ell$ with an isomorphism $\iota \colon E \cong \mathbb{C}$, through which we view $\lambda$ in $E$. Let $\rho \colon \mathrm{Gal}(\Omega/\mathbb{Q}) \to \mathrm{GL}_2(E)$ be irreducible, with continuous trace and determinant, and with $\operatorname{tr} \rho(\mathrm{Frob}_q) = a_q(g)$ and $\det \rho(\mathrm{Frob}_q) = q^{k-1}\chi(q)$ for $q$ outside a finite set.

**Theorem.** There are $m \ge 0$, $E$-linear maps $\pi_i \colon E \otimes \mathrm{Fn}_\ell \to E^2$ and $\sigma_i \colon E^2 \to V_B$ for $i = 1, \dots, m$, and a polynomial $P$ in the admitted Hecke operators with $\lambda(P) = 1$, such that:

- $\pi_i \sigma_j = \delta_{ij}$, and $\sum_i \sigma_i \pi_i$ is the identity on the $\lambda$-eigenvectors in $V_B$;
- $\pi_i$ and $\sigma_i$ commute with the Galois action (through $\rho$ on $E^2$) and with the admitted Hecke operators (through $\lambda$);
- $P$ acts on $V_B$ as $\sum_i \sigma_i \pi_i$.

So the $\lambda$-eigenspace of $V_B$ is $\rho^{\oplus m}$, and $P$ is a Hecke projector onto it.

## Proof

1. `semisimple_potentials_at_newform_eigensystem` gives $\mathrm{SSPotB}$ at weight $w = k - 2$: there is a Hecke polynomial $P$ with $\lambda(P) = 1$ such that $(T - \lambda(T)) P F$ is trivial for each potential $F$ and each admitted $T$. Potentials are polynomial valued functions for the group $\Gamma(N, \ell)$. We have not unfolded the spaces `Pot` and `Triv`.
2. `semisimple_tensor_of_semisimple_potentials` moves this to the tower and gives $\mathrm{SSBB}$: the same $P$ maps $V_B$ into the $\lambda$-eigenspace.
3. `galois_representation_of_eigensystem` uses $\mathrm{SSBB}$, the oddness of $w$ and the hypotheses on $\rho$ to build the maps $\pi_i$, $\sigma_i$ and to prove the conclusion.

The rest is bookkeeping.

## In the Lean code

The theorem is in [HeckeProjectorNewformGaloisImage.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/HeckeProjectorNewformGaloisImage.lean#L12). The three lemmas are restatements, by `exact`, of `SSPotBr.ssPotB_at_newform`, `Comp.ssbb_of_ssPotB` and `HeckeProj.heckeProj_main`. The conditions $\mathrm{SSPotB}$ and $\mathrm{SSBB}$ are in [LiftApplyOfMemAdmissibleSubalgebra.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/LiftApplyOfMemAdmissibleSubalgebra.lean#L14). We have not unfolded the space `X.B` behind $V_B$. The conditions on $\alpha$ are used only in step 1.
