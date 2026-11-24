---
title: Running frames and the growth bound
decls:
  - UpperTheory.HeckeLevelFrameExistence.frameEx_of_fin
  - UpperTheory.BaseChangeIdentities.FrameWordIdentity.wordId
  - UpperTheory.BaseChangeIdentities.FrameWordIdentity.frameBound
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Running frames and the growth bound

Section 16 built a frame for every automorphic representation $\pi$ of $U(n)$ and showed how a character of the operator algebra of a run of the frame is read off. This section supplies the two remaining inputs of the base change theorem of the next section. First, every frame can be run on every finite set of places, given the trace formula of $U(n)$ on the unitary side and a finiteness statement for the candidates of Section 16. Second, on a run, the traces of powers on the finite-dimensional unitary side grow at most like the norms of powers on the block side. The second statement is proved from a word identity, which writes such a trace as a combination of elliptic sums on the blocks $\mathrm{GL}_a \times \mathrm{GL}_{n-a}$. Both results belong to the step [base change for $\mathrm{GL}_n$](/step/base-change-n/), below [every character](/step/every-character/).

We keep the notation of Section 16: $E$ is a CM field with maximal real subfield $F$ in which every finite place is unramified over $F$, a frame $F_0$ for $(\pi, S)$ consists of the data 1 to 10 of Section 16, and a run of $F_0$ on a finite set $T$ of places consists of a local datum $d$, a power $m \ge 1$, a family $\sigma$ of local representations of $U(n)$, the blocks $H_i$ with commuting normal generators $g_x$ and operators $\beta_i$, and a joint eigenvector $v$ in $\mathbb{C}^d$. A run also carries a unitary operator $u$ on $\mathbb{C}^d$ and, for each generator, its operator on the unitary side; we write $g_x = ((g_{x,i})_i, c_x)$ with $c_x$ the operator on $\mathbb{C}^d$. A run satisfies the structure conditions if its pieces have the algebraic properties used in Section 16; we do not list them.

### Runs exist

**Definition 7.25.1 (Unitary side).** The unitary side holds if the following is true for every CM field $E$ as above, $n \ge 1$, section $\mathrm{Sec}$, family $\lambda$ of dominant weights at the archimedean places and level family $K'$ of $U(n)$. There is a finite family $(\pi_i, \sigma_i)_{i \in I}$ with:

1. each $\pi_i$ automorphic of weight $\lambda$ and level $K'$ on $\mathrm{Sec}$, with local components $\sigma_{i,w}$ at $w \in \mathrm{Sec}$ that have nonzero $K'_w$-fixed vectors and finite-dimensional fixed vectors under every open subgroup;
2. every automorphic $\pi'$ of weight $\lambda$ and level $K'$ on $\mathrm{Sec}$ has the components $\sigma_{i,w}$ at all $w \in \mathrm{Sec}$ for some $i$;
3. for every test function $f = (f_w)$ of level $K'$ that at some $w \in \mathrm{Sec}$ is supported on elements with separable characteristic polynomial,
$$\sum_{i \in I}\prod_{w \in \mathrm{Sec}}\mathrm{tr}\,\sigma_{i,w}(f_w) = \mathrm{Geom}(\lambda, f),$$
where the traces are twisted traces on the fixed vectors and $\mathrm{Geom}$ is the geometric side of the trace formula of $U(n)$.

**Definition 7.25.2 (Finiteness of candidates).** Let $F_0$ be a frame for $(\pi, S)$ and $T'$ a finite set of nonsplit places outside $S_0 \cup \mathrm{Bad}$. For local data $c$, $e$, $b$ at the places, let $d = F_0(T', c, e, b)$ be the local datum of the run on $T'$. For isobaric data $P_a$, $P_b$ of ranks $a$, $b$ and $w \in T'$, a pair $(\xi_a, \xi_b)$ is a Jacquet eigenvalue of $(P_a, P_b)$ at $w$ if the Iwahori fixed vectors of the local product of $P_a$ and $P_b$ at $w$ contain a nonzero joint eigenvector of the double coset operators of $\varpi^x \times \varpi^y$, for strictly decreasing $x$ and $y$, with the eigenvalues determined by $\xi_a$ and $\xi_b$ (the condition is not unfolded further). The candidates of a frame are finite if for all such $T'$, $c$, $e$, $b$:

1. for each chain index $i$ and $w \in T'$, the Jacquet eigenvalues at $w$ of the parts $(P_a, P_b)$ of all candidates for $(d, i)$ lie in a finite set;
2. for each $w \in S_0$ there are finitely many isobaric data $D_1, \dots, D_k$ of rank $n$ such that the local product of the datum $D$ of any candidate has the same irreducible subquotients at $w$ as some $D_j$, and the same finite dimension of fixed vectors under the level $K'_w$;
3. the dimension of the Iwahori fixed vectors at $w \in T'$ of the local products of the parts of candidates is bounded.

**Theorem 7.25.3 (Runs of frames).** Assume the unitary side and the finiteness of candidates. Let $E$ be a CM field in which every finite place is unramified over $F$, $n \ge 1$, $\pi$ an automorphic representation of $U(n)$, $S$ a finite set of places, $F_0$ a frame for $(\pi, S)$, and $T$ a finite set of places. Then $F_0$ has a run on $T$.

Lean: `UpperTheory.HeckeLevelFrameExistence.frameEx_of_fin`.

*Proof.* The theorem is a general existence theorem for runs with eighteen hypotheses, of which two are the assumptions. The other sixteen are proved results, some used twice: the commutative local Hecke algebras, with the statements that spherical vectors are unique for them and that the spectral trace of the unitary model is given by them; the Iwahori levels of frames at inert places and the fact that inert places lie in the section; a cone statement for the eigenvalues at inert places, from the [inert eigenvalues](/entry/eig-inert/) and a base change statement for Weyl groups; the comparison of Satake parameters of components; the independence of candidates from auxiliary choices; statements on the local letters, the twisted constant terms, the values of the characters $\mu_w$ and the powers of eigenvalues; and the statement that a finite combination of Iwahori functions is a Hecke function. The last is proved directly: the function attached to the Iwahori coefficients $c$ at $w$ is
$$\sum_{x}c(x)\,[I_w : K_w]\,f_{\varpi^x},$$
a finite sum of Hecke functions, so it is a Hecke function. We did not unfold the general existence theorem or the other inputs. $\square$

### The word identity

Fix a run of $F_0$ on $T$ that satisfies the structure conditions. For a word $\omega$ in the generators and their adjoints, let $\omega_U$ be the product of the corresponding operators on $\mathbb{C}^d$. For a chain index $i$ with $a = a_i$, let $\omega_i$ be the word in the block generators obtained by writing $m$ copies of $\beta_i$ followed by the letters of $\omega$ as block generators of $H_i$. For a nonempty list $\Omega = (\omega_1, \dots, \omega_r)$, let $\Phi_i(\Omega)$ be the matrix of test functions on $\mathrm{GL}_a(\mathbb{A}_E) \times \mathrm{GL}_{n-a}(\mathbb{A}_E)$ of the word $t_{1,i}\,\omega_{1,i}\cdots\omega_{r,i}\,t_{2,i}$, where $t_{1,i}$ and $t_{2,i}$ are the outer operators of the block, with size parameters $T_i(\Omega)$ and $r_i(\Omega)$. Let $\mathrm{sc}_i(\Omega)$ be the product of the scalars of the letters, $M_i$ the matrix of the archimedean data $A_i$, and $\mathrm{Ell}_i$ the sum of the regular elliptic orbital terms of [the elliptic formula](/entry/ell-formula2-j/) on $\mathrm{GL}_a \times \mathrm{GL}_{n-a}$ with the Haar measures of the chain.

**Theorem 7.25.4 (Word identity).** Assume the identity for local words and local matching for words described below. For every frame and every run with the structure conditions there are $c_i \in \mathbb{C}$ and $c_{0,i} \ge 0$, for the chain indices $i$, such that for every nonempty list $\Omega$ of words:

1. for every $i$, $\mathrm{tr}_{M_i}\Phi_i(\Omega)$ is a test function of size $c_{0,i}(1 + T_i(\Omega)) + r_i(\Omega)$;
2. the trace on $\mathbb{C}^d$ satisfies
$$\begin{aligned}&\mathrm{tr}\big(u^r\,\omega_{1,U}\cdots\omega_{r,U}\big)\\ &\quad= \sum_i c_i\,\mathrm{sc}_i(\Omega)\,\mathrm{Ell}_i\big(\mathrm{tr}_{M_i}\Phi_i(\Omega)\big).\end{aligned}$$

Lean: `UpperTheory.BaseChangeIdentities.FrameWordIdentity.wordId`.

The two hypotheses are local. The identity for local words says, for a local datum $d$ and a list of letters with $N + 1$ letters of the first kind, that the product of the local letters for $\mathrm{GL}_a \times \mathrm{GL}_{n-a}$ has, at each bad place, the trace of $\mathrm{fix}_a\,\beta^N$; that at the other places it has the local word of the letters at that place; and that no letter sits at a place that is not good. Local matching for words says that, for unitary letters with the same spherical parts as the local letters off the bad places, the unitary family of test functions matches the product of the local letters at every place of the section with the character $\mu_w$, that both are test functions, and that at some nonsplit place of the section the product is regular.

*Proof.* The proof assembles about fifteen statements on words: the frame words have length one in the letters of the first kind; products of local letters are well formed; the adelic word of a list is built from its archimedean part, its finite part and the local products; the archimedean part of a word is a scalar times the product of the archimedean letters, by the Hermitian property at infinity; the block test functions satisfy the size bound 1; and the trace on the unitary side is computed through the unitary words, the adjoint property of the unitary operators and the elliptic homomorphism of the chain. A general statement combines the test bound with the trace computation into the word identity. We did not unfold these statements. $\square$

### The growth bound

**Theorem 7.25.5 (Growth bound on a run).** Let $F_0$ be a frame for an automorphic representation $\pi$ of $U(n)$ and consider a run with the structure conditions, with marked generator $g_{x_0}$. Let $a = (a_1, a_2)$ be an element of the $*$-algebra generated by the $g_x$ that has the form $b\,g_{x_0}$ with $b$ in that algebra. Then there are $C$, $N$ and $j$ such that for all large $k$
$$\big|\mathrm{tr}\big((u\,a_2)^k\big)\big| \le C(1 + k)^N\max_i\big\|(\beta_i^m a_{1,i})^{k-j}\big\|.$$

Lean: `UpperTheory.BaseChangeIdentities.FrameWordIdentity.frameBound`.

*Proof.* The identity for local words and local matching for words hold: the second is deduced from the first and from three matching statements, the matching of the frame functions at bad places of [Section 7.5.3](/entry/positivity-theory-rg-bc-b-f-match-all-match-lmb2/), the matching of spherical words at split places, and the matching of units. So the word identity holds. A general bound converts the word identity into the growth bound, using the commutation of $u$ with the diagonal operators; we did not unfold it. $\square$

**Remark 7.25.6 (Formalization).** The existence of runs is at [FrameExOfFin.lean](lean:Development/AutomorphicArithmetic/Foundations/BaseChangeIdentities/FrameMatching/HeckeEigenvalueFiniteness/FrameExOfFin.lean#L43). It applies `frameEx_of`, which is proved, with `maxHeartbeats 1000000`, in a file named KUEqKLOfNotMemBad.lean (line 116); the name of the file describes a lemma, not the theorem. The finite sum statement `gcHecke` is in the same file (line 34). The statement `FrameEx` (FrameBoundSpaces/FrameBound.lean:29) and the finiteness `CandFin` (StrictJoinCandidates/CandSt.lean:22) are quantified over a proof of the reading limit `Rd.ReadLimit`, as is `FrameEx0` in Section 16; the unitary side `USide` is in SimpleTwistedTraceFormulaStable.lean:239, in the namespace of abelian varieties. A second `FrameEx` with a different statement is in DescentOffTorusOfFrame.lean:69. The word identity and the growth bound are at [FrameBound.lean](lean:Development/AutomorphicArithmetic/Foundations/BaseChangeIdentities/FrameMatching/HeckeWordBounds/FrameBound.lean#L30) (lines 30 and 42). `WordId`, `LocWord` and `LocMatch` are in WordFrameBounds/WordIdAt.lean (lines 39, 47 and 83), and the bound is `GBound` (DataExOf.lean:52), also quantified over the algebra laws `DiagAlg` of block diagonal operators. `FrameBound` assumes that $\pi$ is automorphic, but `WordId` does not use it. In part 2 of the word identity the power of $u$ is `ws.length`, the number of words, not the number of letters.
