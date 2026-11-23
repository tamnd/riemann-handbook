---
id: wach-lattices
title: Wach-type lattices for an integral block, with a reduced filtration
kind: theorem
decl: GlobalTheory.WachPlace.wach_lattices
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.WachLatticesRankOneModelsReducedFiltration
covers: 889
status: drafted
drafted_by: writer@claude
---
This theorem proves the [Wach lattices of rank one models with a reduced filtration](/entry/wach-lattices-rank-one-models-reduced-filtration/), a second name for it, which goes up to the [Wach inputs](/entry/wach-inputs/) of a crystalline block. It makes Wach-type matrices for a crystalline representation and its rank one pieces, and a filtration of their reductions. The real work is in [the global positions lemma](/entry/exists-positions-global/).

## Statement

Let $E$ be a CM field and $\ell \neq 2$ a prime that does not divide the discriminant of $E$. Let $\sigma$ be a permutation of the embeddings $\tau \colon E \to \overline{\mathbb{Q}}_\ell$ with $|\sigma\tau(x) - \tau(x)^\ell| < 1$ on $\mathcal{O}_E$. Let $J(\tau, a) \in [0, h]$ for $a < n$, and $\mathrm{bot}(\tau) + s \in [0, h]$ for $s < t$. Assume `BhattScholzeCrystallineLattices` and an *integral block*: a finite $L/\mathbb{Q}_\ell$ containing $\mu_\ell$ and all $\tau(E)$; a crystalline $r \colon G_E \to \mathrm{GL}_n(\mathcal{O}_L)$ with Hodge-Tate weights $J(\tau, \cdot)$; crystalline characters $\psi_s$ with weight $\mathrm{bot}(\tau) + s$; and an $r$-stable chain $\varpi \mathcal{O}_L^n = M_0 \subseteq \dots \subseteq M_R = \mathcal{O}_L^n$ with distinct steps $r_s$ where $M_{r_s + 1} = M_{r_s} + \mathcal{O}_L x_s$ and $r(g)x_s \equiv \psi_s(g) x_s \bmod M_{r_s}$.

Then there are a complete domain $\mathcal{O}'$ over $\mathbb{Z}_\ell$ with a map to a field $F$ of characteristic $\ell$, a unit $u = 1 + \ell c$ of $\mathbb{Z}_\ell$ with $c$ a unit, a series $u_n$ with `IsUn`, a primitive $\ell$-th root of unity $\zeta$, maps $j_b$ with `IsLocExp` at $\zeta^b - 1$, and data $N$ (rank $n$) and $N_{\psi,s}$ (rank one) such that:

1. $N$ satisfies `LatN` with weights $J$ and height $h$, and each $N_{\psi,s}$ with weight $\mathrm{bot} + s$;
2. the reductions to $F$ satisfy `RedFilt`: for each $\tau$ there is a flag of $F((X))^n$ from $0$ to the whole space, stable under the reduced $\varphi$ and $\gamma$, with $t$ steps that each add a line on which $\varphi$ and $\gamma$ act through $N_{\psi,s}$ up to a power of $X$.

Here a `Lat` is a triple $(P_\tau, D_\tau, \Theta_\tau)$: matrices over $\mathcal{O}'[[X]]$ for Frobenius and for $\gamma$, and a constant matrix. `LatN` says that $P_\tau(\pi_0)$ divides $q^h$, that $D_\tau \equiv \Theta_\tau$ mod $X - \ell$, and that after each $j_b$ the matrix $P_\tau$ has elementary divisors $X^{J(\tau,a)}$ in a basis compatible with $\gamma$. These objects have the shape of Wach modules (Berger, Compos. Math. 140, 2004); we have not checked them against that source.

## Proof

1. $\mathcal{O}_L$ is a complete discrete valuation ring of residue characteristic $\ell$ (`FinExtIntegers.dvr_complete`).
2. `T.stable_lattice_chain_with_lines_matrix_form` turns the chain into matrices and reduced ranks, with a jump of one at each $r_s$.
3. `T.exists_unit_root_cyclotomicExpExpansions` gives $u$, $c$, $\zeta$ and the $j_b$; `unit_series_constant_holds` gives $u_n$.
4. [`exists_positions_global`](/entry/exists-positions-global/) gives $N$, $N_\psi$ and reduced vectors that form a chain. This is the only use of the published input.
5. `filtration_of_chain` turns the chain into the flag of `RedFilt`.

The witnesses are $\mathcal{O}' = \mathcal{O}_L$, $F$ its residue field and $L' = L$. The rest is bookkeeping.

## In the Lean code

The theorem is in [WachLatticesRankOneModelsReducedFiltration.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/WachLatticesRankOneModelsReducedFiltration.lean#L39). `IntegralBlock` and `RedFilt` are in [IntegralBlock.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IntegralBlock.lean#L22). `Lat`, `IsUn`, `IsLocExp` and `LatN` are in [LemmaWFromLattice.lean](lean:Formalism/PieriBlockIdeals/LemmaWFromLattice.lean#L355).

The conclusion does not name $r$, $\psi$ or the chain $M$: it says only that lattices with the given weights exist and that their reductions have some flag, with a new length $R$ and new positions $r_s$. For $t = 0$, the flag $0 \subseteq F((X))^n$ already satisfies `RedFilt`. The link to $r$ is in the proof, not in the statement.
