---
id: mem-hf-d-of-lattice
title: From an A_inf coboundary to H^1_f, for a map of lattices
kind: theorem
decl: GlobalTheory.Cyc.ClassBound.mem_HfD_of_lattice
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.CrystallineExtensionClassBound
covers: 401
status: drafted
drafted_by: writer@claude
---
This lemma is the last step of [the class bound](/entry/class-bound/). It takes a cocycle $f$ with values in a lattice $T_Y$, whose $\ell^N$-multiple is a coboundary with coefficients $A_{\inf}/\xi^{e+1}$, and a $G_K$-map $\varphi \colon T_Y \to V/T_V$. It puts $\ell^c\, \varphi \circ f$ in $H^1_f(K, V/T_V)$. It only chooses coordinates; the work is in [the coordinate version](/entry/mem-hf-d-of-is-cob/).

## Statement

Notation as in [the class bound](/entry/class-bound/): $K$, $L$, $s$, $K_s$, $\chi$, lattice representations, and $H^1_f$. Let $G_{K_s} \subseteq G_K$ be the fixing groups. Assume local Tate duality and Tate's Euler characteristic formula (`adm2 D`, `ArchimedeanSignatureMatching D`), $s \geq 1$ with $s \geq 2$ if $\ell = 2$, and $K \subseteq K_s$. Let $e, N \geq 0$, and let $Y$, $V$ be lattice representations of $G_K$ over $L$ with $g \cdot x = \chi(g)^{-e} x$ on $V$. Let:

- $\varphi \colon T_Y \to V/T_V$ be $\mathcal{O}_L$-linear and $G_K$-equivariant;
- $f \colon G_K \to T_Y$ be a cocycle, locally constant modulo $\ell^n$ for each $n$;
- $\ell^N (f \otimes 1)$, restricted to $G_{K_s}$, be a coboundary in $T_Y \otimes_{\mathbb{Z}_\ell} A_{\inf}/\xi^{e+1}$.

Then $g \mapsto \ell^{c} \varphi(f(g))$ lies in $H^1_f(K, V/T_V)$, with
$$c = N + (e+2)s + v_\ell(e) + \lfloor e/(\ell-1) \rfloor + 1 + s + v_\ell(e+1) + g_K, \qquad g_K = v_\ell[K_s:\mathbb{Q}_\ell] - v_\ell[K:\mathbb{Q}_\ell].$$

## Proof

1. `LatBasis.exists_basis`: $V$ has a $\mathbb{Q}_\ell$-basis $w$ such that $x \in T_V$ if and only if all coordinates of $x$ are in $\mathbb{Z}_\ell$, and the coordinate maps are continuous. The same holds for $Y$, with a basis $u$.
2. `exists_coords`: $T_Y$ is free, so $\varphi$ lifts to an additive map $\Phi \colon T_Y \to V$. Its coordinates $\psi_i = w_i^* \circ \Phi$ are $\mathbb{Z}_\ell$-linear and bounded by $\ell^r$ for one $r$. The bound holds on the $u_j$, so on $T_Y$ by the ultrametric inequality.
3. `lift_equivariant`: since $\varphi$ is equivariant, $\Phi(gy) - g\Phi(y) \in T_V$.
4. [`mem_HfD_of_isCob`](/entry/mem-hf-d-of-is-cob/) gives $\ell^{g_K} [\ell^k \Phi(f(g))] \in H^1_f$, with $k = c - g_K$.
5. `pow_smul_eq_mk`: $\ell^{k + g_K} \varphi(y) = \ell^{g_K} [\ell^k \Phi(y)]$.

## In the Lean code

The lemma is at [CrystallineExtensionClassBound.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/CrystallineExtensionClassBound.lean#L327). The lemmas it calls:

- `GlobalTheory.Cyc.LatBasis.exists_basis`, in ExistsBasisOfSubmodule.lean;
- `exists_coords`, `lift_equivariant`, `pow_smul_eq_mk` and `mem_HfD_of_isCob`, in the same file.

The exponent is written `cTB l s e g N`, from [LocalSituation.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/LocalSituation.lean#L25). The action on $V$ is given as $\bigl(\chi(g)^{-1}\bigr)^e$ with $\chi$ of the period data at $K$. The proof rewrites it with `PD_χ` to $\chi_{\mathbb{Q}}(g)^{-e}$ for the character on all of $G_{\mathbb{Q}_\ell}$. The lattice $T_Y$ is made a $\mathbb{Z}_\ell$-module through $\mathcal{O}_L$ (`zlMod`). `adm2` and `ArchimedeanSignatureMatching` are only passed down.
