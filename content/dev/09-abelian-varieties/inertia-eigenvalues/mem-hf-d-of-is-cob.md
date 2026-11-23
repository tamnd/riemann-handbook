---
id: mem-hf-d-of-is-cob
title: From an A_inf coboundary to H^1_f, in coordinates
kind: theorem
decl: GlobalTheory.Cyc.ClassBound.mem_HfD_of_isCob
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.CrystallineExtensionClassBound
covers: 397
status: drafted
drafted_by: writer@claude
---
This lemma does the work of [the lattice lemma](/entry/mem-hf-d-of-lattice/) once $V$ has coordinates. It treats each coordinate with [the scalar lemma](/entry/scalar-of-is-cob/), then puts the coordinates together and passes from $G_{K_s}$ to $G_K$.

## Statement

Notation as in [the lattice lemma](/entry/mem-hf-d-of-lattice/), with the same hypotheses on $D$, $s$ and $K$. Let $e, N, r \geq 0$. Let $Y$ be a $\mathbb{Z}_\ell$-module with an action $\rho$ of $G_K$. Let $f \colon G_K \to Y$ be a cocycle, locally constant modulo $\ell^n$ for each $n$, such that $\ell^N (f \otimes 1)$ is a coboundary on $G_{K_s}$ in $Y \otimes A_{\inf}/\xi^{e+1}$. Let $V$ be a lattice representation on which $G_K$ acts by $\chi^{-e}$. Let $w_1, \dots, w_n$ be a $\mathbb{Q}_\ell$-basis of $V$ with $T_V = \{x : \text{all coordinates in } \mathbb{Z}_\ell\}$, with continuous inverse coordinate map. Let $\Phi \colon Y \to V$ be additive with $\Phi(\rho(g) y) - g\Phi(y) \in T_V$, and suppose that its coordinates $\psi_i = w_i^* \circ \Phi$ are $\mathbb{Z}_\ell$-linear and bounded by $\ell^r$.

Then $g \mapsto \ell^{g_K} \bigl[\ell^k \Phi(f(g))\bigr]$ lies in $H^1_f(K, V/T_V)$, where
$$k = N + (e+2)s + v_\ell(e) + \lfloor e/(\ell-1) \rfloor + 1 + s + v_\ell(e+1), \qquad g_K = v_\ell[K_s:\mathbb{Q}_\ell] - v_\ell[K:\mathbb{Q}_\ell].$$

## Proof

1. Each $\psi_i$ is equivariant up to $\mathbb{Z}_\ell$: $|\psi_i(\rho(g)y) - \chi(g)^{-e} \psi_i(y)| \leq 1$. This follows from the equivariance of $\Phi$ modulo $T_V$ and the choice of $w$.
2. [`scalar_of_isCob`](/entry/scalar-of-is-cob/), applied to each $\psi_i$, gives a cocycle $z_i \colon G_{K_s} \to \mathbb{Q}_\ell(-e)$ and $x_i \in B$ with $z_i(\sigma) = \chi(\sigma)^{-e}\sigma(x_i) - x_i$, and $|z_i(g) - \ell^k \psi_i(f(g))| \leq 1$ on $G_{K_s}$.
3. `mem_HfD_of_coords` ends the proof. It forms $Z = \sum_i z_i w_i$. This is a continuous cocycle on $G_{K_s}$, and $Z \otimes 1$ is the coboundary of $\sum_i w_i \otimes x_i$ in $V \otimes B$ (`actVB_sum_tmul`). $Z$ agrees with $f_0 = \ell^k \Phi \circ f$ modulo $T_V$, and $f_0$ is a cocycle modulo $T_V$. Then `pow_smul_mem_HfD_of_restriction` passes from the open normal subgroup $G_{K_s}$ to $G_K$, at the cost of $\ell^{v_\ell[G_K : G_{K_s}]}$. By `layer_group`, this valuation is $g_K$.

## In the Lean code

The lemma is at [CrystallineExtensionClassBound.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/CrystallineExtensionClassBound.lean#L257). The lemmas it calls:

- `scalar_of_isCob` and `mem_HfD_of_coords` (line 108), in the same file;
- through `mem_HfD_of_coords`: `actVB_sum_tmul`, `GlobalTheory.Cyc.LayerGroup.layer_group` and `GlobalTheory.pow_smul_mem_HfD_of_restriction`, in PowSmulMemHfDOfRestriction.lean. We have read the statement of the last one, not its proof.

The group $G_{K_s}$ is `Gj K s`, a subgroup of the full Galois group $G_{\mathbb{Q}_\ell}$; `hle` says that it lies in $G_K$. The proof chooses the $z_i$ and $x_i$ with `choose` and fixes $k$ with `generalize`.
