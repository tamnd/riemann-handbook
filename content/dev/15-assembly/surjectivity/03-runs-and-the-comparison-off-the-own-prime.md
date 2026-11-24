---
title: Runs and the comparison off the own prime
decls:
  - GlobalTheory.BigOn.RunsExist.exists_runs_at_alt
  - GlobalTheory.BigOn.bigOn_runsSt
  - GlobalTheory.T.runs_estimate_statement'
  - GlobalTheory.BigOn.compareOffOwn_atRuns_alt
  - GlobalTheory.ShareOn.modelSt_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Runs and the comparison off the own prime

This section proves three statements at the rich points of a family. The first gives a good pair of runs at each rich point. The second compares a trace lattice of cusp forms with the theta base lattice at the twisted places, after localization at each prime that is not above the own prime of the place. The third gives a model of the cusp forms along each pair of runs. All three hold with no hypothesis. The surjectivity statement of [Section 5.10.7](/entry/onto-x-of-hypotheses-alt-alt/) uses the comparison for the rank statement and the run model for the share statements; [the last step of its proof](/entry/onto-x-of-twist-shares-exp-alt/) uses the runs and the comparison again.

Let $p$ be a point of a family. The host field $E$ of $p$ has two special primes $p_1$ and $p_2$. For a finite place $v$ the *own prime* $\ell_v$ of $v$ is $p_1$ if the residue characteristic of $v$ is $p_1$, and $p_2$ otherwise.

**Definition 5.3.1 (Pair of runs).** A *pair of runs* at $p$ is a triple $r = (r_1, r_2, \ell)$ of a parameter run $r_1$ at $p_1$, a parameter run $r_2$ at $p_2$ and a level structure $\ell$ for the finite group of $p$. At a place $v$ the *used run* is $r_1$ if the residue characteristic of $v$ is $p_1$, and $r_2$ otherwise. The pair is *good* if, at each place $v$, the used run satisfies the full laws, the core and extra conditions and the pins at $v$, and the level structure fixes the used run in the two ways that the level conditions ask, and the level ties hold. The pair is *pinned at the own primes* if the runs $r_1$ and $r_2$ are pinned at their primes.

Lean: `GlobalTheory.BigOn.TwoRuns` (also `GlobalTheory.BigOn.RunsOk` and `GlobalTheory.BigOn.OwnPin`).

**Lemma 5.3.2 (Runs at a point).** Let $p$ be a regular and rich point. Then there is a good pair of runs at $p$ that is pinned at the own primes.

Lean: `GlobalTheory.BigOn.RunsExist.exists_runs_at_alt`.

*Proof.* The places of single index of $p$ are twisted, so $p$ has links. The links and the core ties give, at each of the two special primes, a parameter run with the full laws, the core and extra conditions, the pins and a pin at the prime. Call them $r_1$ and $r_2$, with pins $d_1$ and $d_2$. The core of the links and the level of the core ties give a level structure $\ell$ for the finite group that fixes each run with the full laws. Put $r = (r_1, r_2, \ell)$. It is pinned at the own primes by $d_1$ and $d_2$. At a place $v$ the used run is $r_1$ or $r_2$, and in each case the conditions at $v$ are those of that run. The level ties come from the core ties. $\square$

**Definition 5.3.3 (Two runs statement).** The *two runs statement* is the closed property: eventually at the points of $\mathcal{F}$, each rich point has a good pair of runs that is pinned at the own primes.

Lean: `GlobalTheory.BigOn.TwoRunsStatement`.

**Theorem 5.3.4 (Runs along a family).** The two runs statement holds.

Lean: `GlobalTheory.BigOn.bigOn_runsSt` (also `GlobalTheory.T.runs_estimate_statement'`, a second name).

*Proof.* Take $\varepsilon_1 = 1$, the zero threshold record and $x_0 = 0$. At each regular rich point the lemma gives the runs. $\square$

Next we compare lattices. Let $p$ be a point with a pair of runs, let $v$ be a twisted place and $j$ a level. Let $U = P_0$ be the group of the face of $p$ and $\psi = \psi_0^{-1}$ its character. Let $L$ be the coefficient field. The *trace lattice* at $v$ and $j$ is

$$T_j = \operatorname{span}_{\mathcal{O}_L} \Big\{ \sum_{u \in U} \psi(u)\, c\big(f(u)\big) \Big\},$$

where $f$ runs over the orbit families of cusp forms of index $j + 1$ and weight $\kappa_j$, and $c$ is the coefficient map into $L^{n_W(j)}$. The *theta base lattice* $\Theta_v$ at $v$ is the lattice of theta series of the first phase at $v$.

**Theorem 5.3.5 (Comparison off the own prime).** Eventually at the points of $\mathcal{F}$, for each rich point $p$, each good pair of runs $r$ at $p$ that is pinned at the own primes, each twisted place $v$ and each level $j$, the following holds. For each prime $\lambda$ of $\mathcal{O}_L$ with residue characteristic different from $\ell_v$,

$$(T_j)_\lambda \subseteq (\Theta_v)_\lambda.$$

Lean: `GlobalTheory.BigOn.compareOffOwn_atRuns_alt` (also `GlobalTheory.T.bigOn_comparison_at_twisted_places`, a second name).

*Proof.* Along the family, eventually five numerical bounds hold at the point; we use only the last, $8 f r + 4 \le n_V$. Let $p$ be a rich point beyond the threshold. The places of single index are twisted, so $p$ has links: the core data, a uniformity, the pins and the phases. The class sums span, by the bound $8 f r + 4 \le n_V$ and the core. The values of the character $\delta$ at the place of $v$ lie in the image of $L$. The elements of $U$ have determinant $1$, since they lie in the base group. Now the pointwise comparison, [the trace lattice lies in the span of theta series away from the own prime](/entry/trace-lattice-le-span-theta-series-away-from-own-prime/), gives the inclusion from these facts and from the run, level and action pins of $r$. $\square$

The inclusion says nothing at the primes over $\ell_v$. There, the lattices are compared in the export statement of Section 4 and the twist bound of Section 10.

Last, the run model. For a pair of runs $r$ at $p$ and an index $i$, a *run model* at $(p, i)$ consists of a constant $C$, a finite space $M$ of cusp forms with an action, a level datum $\kappa$ and a model relation between $M$ and the used runs. A *reading* of the run model is a semilinear map from a coefficient space onto $M$ with three conditions on its image and its kernel, and a count: the set $\Psi$ of the reading has $f$ elements.

**Definition 5.3.6 (Run model statement).** The *run model statement* is the closed property: eventually at the points of $\mathcal{F}$, for each rich point $p$, each good pair of runs $r$ pinned at the own primes and each index $i$, there is a run model $(C, M, \kappa)$ at $(p, i)$ with a reading, the level condition restricted to the half unipotent part holds, $|\Psi| = f$, and the alternative at $p_0$ holds: either $p_0$ is extreme or the archimedean condition holds for the model.

Lean: `GlobalTheory.ShareOn.ModelStatement`.

**Theorem 5.3.7 (Run models).** The run model statement holds.

Lean: `GlobalTheory.ShareOn.modelSt_alt`.

*Proof.* Two closed statements hold with no input: the alternative at $p_0$ for each run model, and the bound that the type primes are greater than $3$. Join them, and take the larger height threshold. Let $p$ be a rich point beyond it, with a pair of runs $r$ and an index $i$. There is a run model $(C, M, \kappa)$ at $(p, i)$. The number of bad places of the datum at $(x, i)$ is positive: a place $v$ of the model is bad at the field of $p$. So there is a reading of the model, with $|\Psi| = f$; this uses the lower bound on $n_V$ in the family parameters. The bound on the type primes gives the level condition on the half unipotent part. The alternative at $p_0$ is the first closed statement. $\square$

**Remark 5.3.8 (Formalization).** The runs are in [ExistsRunsAt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsRunsAt.lean#L18). The theorem at lines 56 to 58 proves a closed statement with $\varepsilon_1 = 1$, the zero record and $x_0 = 0$: the statement has no content along the family beyond the lemma at each point. Its second name in ExistsRunsAtStatement.lean is a one-line call with `maxHeartbeats` set to 1000000. The comparison is in [CompareOffOwnAtRuns.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/CompareOffOwnAtRuns.lean#L14); it uses the numerical bounds along the family at parameter $0$ and keeps one of the five. The condition "not above $\ell_v$" is an inequality of residue characteristics. The run model statement is in [ShareWSt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ShareWSt.lean#L21) and the theorem in [ModelSt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ModelSt.lean#L19). There is a second, different definition with the same last name, the model statement of Section 8, in ModelStatement.lean at line 26. We have not unfolded the runs, the laws and pins, the run model, the reading, the theta base lattice or the orbit families.
