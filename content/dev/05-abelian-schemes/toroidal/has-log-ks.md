---
id: has-log-ks
title: The log Kodaira-Spencer isomorphism on a smooth toroidal model
kind: theorem
decl: GlobalTheory.LogKSAssembly.hasLogKS
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.LogKodairaSpencerIsoSmoothSncToroidalModel
covers: 2263
status: drafted
drafted_by: writer@claude
---
This theorem gives the log Kodaira-Spencer isomorphism on a model $Y$ of the moduli scheme. It proves [the statement form](/entry/log-kodaira-spencer-iso-smooth-snc-toroidal-model/), which [`toroidalForFanKS_of_rigidForFan`](/entry/toroidal-for-fan-ks-of-rigid-for-fan/) uses to get the last clause of `ToroidalForFanKS`.

## Statement

Let $Y$ be a model of $X^\circ_F$ over $F$, as in [`toroidalForFanKS_of_rigidForFan`](/entry/toroidal-for-fan-ks-of-rigid-for-fan/), for a datum of signature $(p, q)$. It carries a semi-abelian scheme $G \to Y$, abelian exactly over $X^\circ_F$, with a rigidified line bundle $L$ with trivializations on opens $U_\alpha$ and transition functions $g_{\alpha\beta}$. Let $n_0 = \tfrac{[E:\mathbb{Q}]}{2} p q$.

**Log derivations.** For an affine open $U$ with ring $R = \Gamma(U)$, let $T_U$ be the $R$-module of derivations of $R$ that kill $F$ and preserve the ideal of the boundary $Y \setminus X^\circ_F$ (`logDer`).

**Frames.** A frame on $U$ is a basis $v_1, \dots, v_n$ of the tangent vectors of $G$ along the zero section over $U$, with the matrices $A(a)$ of the action of $a \in \mathcal{O}_E$ in it. Let $\mathrm{Bal}$ be the module of $n \times n$ matrices $\Theta$ over $R$ with $\Theta^{\mathsf T} = \Theta$ and $A(a)^{\mathsf T}\Theta = \Theta A(\bar a)$ for all $a$ (`balanced`).

**The Kodaira-Spencer relation.** `IsKS D Θ` says: there are an open cover $(W_i)$ of $G$ over $U \cap X^\circ_F$, each $W_i$ inside some $U_{\alpha(i)}$, and derivations $d_i$ on $W_i$ that lift $D$, such that on overlaps

$$d_i f - d_{i'} f = \sum_{a,b} \Theta_{ab} \, \bigl(\partial_{w_b} \log g_{\alpha(i)\alpha(i')}\bigr) \, \partial_{w_a} f,$$

where $w_a$ is the translate of $v_a$ to the point of evaluation. This is a Čech form of the Kodaira-Spencer class of $D$.

**Theorem.** Let $p + q \geq 1$. Assume $Y$ smooth over $F$ of relative dimension $n_0$, with simple normal crossings boundary, and with a rigid chart at each closed boundary point (`HasRigidChart`). Then for each affine open $U$ and each frame on $U$ there is an $R$-linear isomorphism $e \colon T_U \to \mathrm{Bal}$ with $\mathrm{IsKS}(D, \Theta) \iff \Theta = e(D)$.

This has the form of the log Kodaira-Spencer isomorphism of toroidal compactifications (Faltings and Chai, *Degeneration of Abelian Varieties* (1990), for the Siegel case; Lan, *Arithmetic Compactifications of PEL-Type Shimura Varieties*, 2013, for PEL type). We have not checked that the definitions match.

## Proof

The core is the lemma `exists_equiv`. Let $K$ be a relation between finite projective modules $M$ and $N$. Suppose that each $D \in M$ has a unique $\Theta$ with $K(D, \Theta)$, that $K$ is linear, that each such $\Theta$ is in $N$, that $M$ and $N$ have equal fibre ranks at each maximal ideal $\mathfrak m$, and that $\Theta \equiv 0 \bmod \mathfrak m$ implies $D \in \mathfrak m M$. Then $D \mapsto \Theta$ is an isomorphism (`bijective_of_injective_mod_maximal`).

Take $M = T_U$, $N = \mathrm{Bal}$, $K = \mathrm{IsKS}$. The inputs:

1. `LogDerProj.main`: $T_U$ is finite projective of fibre rank $n_0$;
2. `symmetric_balanced_tensors_finite_projective_rank_dim`: the same for $\mathrm{Bal}$;
3. `exists_kodairaSpencer_regular_framed_affine`: each $D$ has some $\Theta$;
4. `isKS_unique_model`: $\Theta$ is unique;
5. `isKS_linear`: the relation is linear;
6. `ksClass_mem_balanced`: $\Theta$ is balanced;
7. `logKodairaSpencer_injective_mod_maximalIdeal`: injectivity modulo each maximal ideal.

The rest is bookkeeping.

## In the Lean code

The theorem is in [LogKodairaSpencerIsoSmoothSncToroidalModel.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LogKodairaSpencerIsoSmoothSncToroidalModel.lean#L57), `exists_equiv` at [L33](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LogKodairaSpencerIsoSmoothSncToroidalModel.lean#L33). The definitions are in [DenseInterior.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/DenseInterior.lean#L99).

`HasLogKS` says nothing on an affine open with no frame. Inputs 1, 2 and 5 do not take the rigid charts. Inputs 4 and 6 introduce them as `_`, so they appear unused there. So the rigid charts can enter only through inputs 3 and 7, whose proofs we have not opened.
