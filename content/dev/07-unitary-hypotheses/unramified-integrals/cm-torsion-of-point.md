---
id: cm-torsion-of-point
title: Integral unramified torsion values, given a torsion point
kind: theorem
decl: ReciprocityTheory.ChartRestriction.L1.cmTorsion_of_point
module: ReciprocityTheory.ReductiveGroups.UnramifiedIntegrals.TorStatus
covers: 342
status: drafted
drafted_by: writer@claude
---
This theorem proves [CM4](/entry/cm4/) from one input, `TorPt`: the scaled values of $\wp$ and $\wp'$ at a torsion point of the lattice form a torsion point of a Weierstrass curve. It is mostly a wrapper. The local work is in [the unramified torsion coordinates](/entry/tor-kur/).

## Statement

Let $\ell \ge 5$ be prime and $K$ the completion of $\mathbb{Q}_\ell^{\mathrm{ur}}$ in $\mathbb{C}_\ell$. Let $\wp$ be the [[Weierstrass function|361NAK68QK]] of a lattice $L$, and $\iota \colon \mathbb{C} \to \mathbb{C}_\ell$ a field isomorphism. Suppose the scaled invariants $\lambda^4\iota g_2$, $\lambda^6\iota g_3$ lie in $K$, have norm at most 1, and give a discriminant of norm 1. If $z \notin L$ and $Nz \in L$ with $\ell \nmid N$, then $\lambda^2\iota\wp(z)$ and $\lambda^3\iota\wp'(z)$ lie in $K$ and have norm at most 1.

## Proof

1. The hypotheses form a `GoodPair`. `TorPt` gives a point $P \neq O$ with $x = \lambda^2\iota\wp(z)$, $y = \lambda^3\iota\wp'(z)/2$ and $N \cdot P = O$.
2. [The unramified torsion coordinates](/entry/tor-kur/) put $x$ and $y$ in $K$.
3. $P$ is not in the kernel of reduction, so $\|x\|, \|y\| \le 1$. Since $\|2\| \le 1$, the claims follow.

## In the Lean code

The theorem is at [TorStatus.lean](lean:ReciprocityTheory/ReductiveGroups/UnramifiedIntegrals/TorStatus.lean#L15). `CM4` also assumes a squarefree $d \equiv 3 \pmod 4$, complex multiplication of $L$ by $(1+\sqrt{-d})/2$, and $\ell \nmid d$. The first line, `intro d L _ _ _ l _ hl _ ι lam ...`, leaves these unnamed, and the proof never uses them. `TorPt` is in [TorDefs.lean](lean:ReciprocityTheory/ReductiveGroups/UnramifiedIntegrals/TorDefs.lean#L32). I did not unfold the proof of `torPt`.
