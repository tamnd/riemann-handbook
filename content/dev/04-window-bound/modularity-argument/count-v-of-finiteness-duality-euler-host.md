---
id: count-v-of-finiteness-duality-euler-host
title: The case V count from a deformation ring of three-dimensional representations
kind: theorem
decl: UpperTheory.V.UnitaryThreeInertia.countV_of_finiteness_duality_euler_host
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ThresholdArguments.DenseThresholdCases.CountVOf
covers: 601
status: drafted
drafted_by: writer@claude
---
This theorem proves $\mathrm{CountV}$ from thirteen statements. [The case V count from the extended hypotheses](/entry/count-v-of-printed-bound-k-reduced-unitary-lift/) supplies them, and the count goes to `vwin_of_hypotheses_H_E_alt` (Step 5 of the chapter [The window bound VWin](/proof/vwin/)). The idea: bound the length of a Tate-Shafarevich-type group by the congruences between the reducible three-dimensional point $r_0$ and the automorphic points of a universal deformation ring.

## Statement

Fix a host $h$ with modulus $N$, an odd prime $l$, a coefficient ring $\mathcal{O}$ (a finite extension of $\mathbb{Z}_l$), $0 < e$ and a [[Dirichlet character|JR4QSEFXWF]] $\psi$ modulo $N$. Let $e_{\mathcal{O}}$ be the length of $\mathcal{O}/l\mathcal{O}$, and $V(\psi)$ the length `Vlen` of the chapter. $\mathrm{CountV}$ is the count shape of the chapter for case V with $R_1(l, \psi) \le 2^{c_2(\psi)}$: for each primitive $\chi$ there is $C$ such that $V(\psi) < \infty$ and $\tfrac{V(\psi)}{e_{\mathcal{O}}} \log l \le (l N e)^C$ for all such data.

A *host frame* $F$ is a frame on the Galois group $\Gamma_S$ of the maximal extension of $\mathbb{Q}$ unramified outside the primes $S$ dividing $lN$, with the character $\eta$ of $\mathbb{Q}(i)$ and the character $\Psi$ made from $\psi$ and $e$ (`IsHostFrame`), and $r_0$ is the reducible point built from $\eta$ and $\Psi$. Let $K$ be a CM field of degree 2 that contains $i$.

**Theorem.** Assume the following. Then $\mathrm{CountV}$ holds.

1. $\mathrm{ThmS6\_s}$: for each host frame there is a marked $g_1 \in \Gamma_S$ such that for each universal deformation $u$ with ring $R$, the weight 0 part of $R$ is finite over $\mathcal{O}$, and each point $r$ of type I of $R$ satisfies `BPrime_s`: $r$ is irreducible on open subgroups of $\ker \eta$ and on $\ker \eta \cap \ker(\text{cyclotomic})$, and is automorphic over $K$ (`AutOnAlt K ι (-1)`).
2. `LemmaM` and `LemmaM'` (not unfolded).
3. Six [[Galois cohomology|9MPCZ3EAJM]] statements: local finiteness, local Tate duality, local Euler characteristic, global finiteness, global Euler characteristic, Poitou-Tate.
4. `HostVanE`, `HostXpp`: each host frame satisfies `F.VanE` (a vanishing statement for cocycles of $r_0$ of weight $\le 0$) and `F.Xpp` (the Selmer quotient of weight $-2$ has at most one element).
5. `HostRigid_s`: each characteristic zero point with `BPrime_s` is rigid.
6. `HostNumber_s`: there are $C$ and $\varphi \in \Gamma_S$ with $\operatorname{tr} r(\varphi) \ne \operatorname{tr} r_0(\varphi)$ for each good point $r$, and for good points $r_1, \dots, r_n$, pairwise not isomorphic on $\ker \eta$, $\log l \sum_i v_l(\operatorname{tr} r_i(\varphi) - \operatorname{tr} r_0(\varphi)) \le (lNe)^C$, with $v_l(x) = -\log|x| / \log l$.

## Proof

Fix $\chi$. `gaussian_field_range_eq_ker_quartic_char` gives $K$; `HostNumber_s` for $K$ gives $C$. The exponent is $C + 1$, independent of $\chi$. Then `hostData_of_host` and `exists_hostFrame` give a host frame $F$, and we choose $\iota \colon \overline{\mathbb{Q}}_l \cong \mathbb{C}$. $\mathrm{ThmS6\_s}$ gives $g_1$. `hostFrame_ok`, `hostFrame_phi` and `exists_isUniv` give a universal deformation $u$. The main step is [`abstract_count`](/entry/abstract-count/), with inputs `LemmaM`, `LemmaM'`, `hostFrame_locVan`, `hostFrame_count`, `HostVanE`, `frame_class_one`, `HostXpp`, rigidity and $\varphi$. It gives points $r_1, \dots, r_n$ as in 6 and $V$ with $\mathrm{shaLen}(a) \le V$ for $a \ne 0$ and $V \le 2 e_{\mathcal{O}} \sum_i v_l(\dots)$. `vlen_le` gives $V(\psi) \le V$. With $X = lNe \ge 2$, `arith` gives $\tfrac{V(\psi)}{e_{\mathcal{O}}} \log l \le 2X^C \le X^{C+1}$.

## In the Lean code

The theorem is in [CountVOf.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/CountVOf.lean#L33). The hypotheses are in [ThmS6CoreS.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/ThmS6CoreS.lean#L17), [HostNumberS.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/HostNumberS.lean#L12) and [HostNumber.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeDeformations/HostNumber.lean#L9). `abstract_count` is in [AbstractCount.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeDeformations/AbstractCount.lean#L25). We have not unfolded `Frame`, `IsUniv`, `TypeI`, `Rigid` or `tor`.

The private lemmas `arith` and `l_mem` are copies of the same lemmas in [UnitaryThreeDeformations/CountVOf.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeDeformations/CountVOf.lean#L19). That file has nothing else.
