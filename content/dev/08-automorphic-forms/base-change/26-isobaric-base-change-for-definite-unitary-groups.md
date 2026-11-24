---
title: Isobaric base change for definite unitary groups
decls:
  - UpperTheory.BaseChangeIdentities.baseChangeN_of
  - UpperTheory.BaseChangeIdentities.baseChangeN
  - UpperTheory.BaseChangeIdentities.baseChangeNB
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Isobaric base change for definite unitary groups

This section states the main theorem of the chapter: every automorphic representation of the definite unitary group $U(n)$ has a base change to $\mathrm{GL}_n(\mathbb{A}_E)$, given by an isobaric sum of discrete automorphic representations of Speh type, with the expected local components at split and inert places and the expected infinitesimal characters. The theorem is the step [base change for $\mathrm{GL}_n$](/step/base-change-n/), used by [every character](/step/every-character/). Its proof puts together the frames of Section 16, the runs and the growth bound of Section 25, and the reading of characters of Section 16, through the limit statement for infinitesimal characters of Section 08.

Let $E$ be a CM field with maximal real subfield $F$, and $U(n)$ the definite unitary group of Section 24. For a finite place $w$ of $E$ let $E_w$ be the completion, and for an automorphic representation $V$ of $\mathrm{GL}_N(\mathbb{A}_E)$ and an embedding $\tau : E \to \mathbb{C}$ let the infinitesimal character of $V$ at $\tau$ be a multiset of $N$ complex numbers, as in Section 08. For $\alpha = (\alpha_1, \dots, \alpha_{\lfloor n/2\rfloor})$ put
$$\mathrm{bc}_n(\alpha) = \{\alpha_i\} \cup \{\alpha_i^{-1}\} \cup \{1\}^{n - 2\lfloor n/2\rfloor},$$
a multiset of size $n$. A place $w$ of $E$ is inert if its local conjugation $s$ is a nontrivial automorphism of $E_w$ that extends complex conjugation on $E$. At an unramified inert place the Satake parameter of $\pi$ is such an $\alpha$.

**Definition 7.26.1 (Speh type).** An automorphic subrepresentation $V$ of the discrete spectrum of $\mathrm{GL}_N(\mathbb{A}_E)$ is of Speh type if there are a unitary, normalized, conjugate self-dual cuspidal representation $P$ of $\mathrm{GL}_a(\mathbb{A}_E)$ and $d \ge 1$ with $ad = N$, such that $V$ embeds in the space of automorphic forms induced from $P|\det|^{s_1} \otimes \cdots \otimes P|\det|^{s_d}$, where $s_i = (a - 1)e_i$ and $e_i = \frac{d - 1}{2} - i$ for $0 \le i < d$. The model is the [Speh representation](/entry/speh/).

**Definition 7.26.2 (Isobaric base change).** Let $\pi$ be an automorphic representation of $U(n)$. An isobaric base change of $\pi$ consists of $c \ge 0$, ranks $N_1, \dots, N_c$ with $\sum_iN_i = n$, automorphic representations $V_i$ of $\mathrm{GL}_{N_i}(\mathbb{A}_E)$, smooth irreducible representations $\sigma_{i,w}$ of $\mathrm{GL}_{N_i}(E_w)$ and $P_w$ of $\mathrm{GL}_n(E_w)$ for every finite $w$, and multisets $m_i(\tau)$ for every embedding $\tau$, such that:

1. every $N_i$ is positive, and every $V_i$ is discrete and of Speh type;
2. $\sigma_{i,w}$ is the local component of $V_i$ at $w$, and $V_i$ has infinitesimal character $m_i(\tau)$ at $\tau$;
3. $P_w$ is a subquotient of the representation of $\mathrm{GL}_n(E_w)$ induced from $\sigma_{1,w} \otimes \cdots \otimes \sigma_{c,w}$;
4. if $\pi$ is unramified at $w$, then $P_w$ is spherical;
5. if $w$ is inert, unramified for $\pi$ with uniformizer $\varpi$ and residue cardinality $q$, and $\pi$ has Satake parameter $\alpha$ at $w$, then $P_w$ has Satake parameter $\mathrm{bc}_n(\alpha)$;
6. if $w$ is split, then $P_w$ is the component of $\pi$ at $w$ under the identification of $U(n)(F_v)$ with $\mathrm{GL}_n(E_w)$ of Section 15;
7. if $\pi$ has weight $\lambda$ at $\tau$, then $\sum_im_i(\tau)$ is the infinitesimal character of the algebraic representation of highest weight $\lambda$.

We say that $E$ is unramified over $F$ if every finite place of $E$ is unramified over $F$.

### The conditional form

**Theorem 7.26.3 (Isobaric base change from finiteness of candidates).** Assume the finiteness of candidates of Section 25. Let $E$ be a CM field unramified over $F$, $n \ge 1$, and $\pi$ an automorphic representation of $U(n)$. Then $\pi$ has an isobaric base change.

Lean: `UpperTheory.BaseChangeIdentities.baseChangeN_of`.

*Proof.* We go in three steps.

1. Generic inputs. Let $S$ be a set of at most one finite place. We claim that there are a compact open level $K$ of $\mathrm{GL}_n$ and finite-dimensional type spaces $W(N)$ such that for every finite set $T$ of places there is a run, in the sense of Section 16, whose generators satisfy the growth bound of Section 25 and the reading condition of Section 16. This is deduced from: the reading limit, which comes from the limit statement for infinitesimal characters, whose statement is that of [Section 7.8.9](/entry/e-final-of/); the algebra laws of block diagonal operators; the [existence of frames](/entry/frame-ex0/); the [existence of runs](/entry/frame-ex-of-fin/), from the unitary side and the finiteness of candidates; the structure conditions of runs; the [growth bound](/entry/frame-word-identity-frame-bound/); and the reading of characters, from [block candidates](/entry/block-candidates-of-inputs/).
2. Finitely many data. From step 1, the finiteness of the discrete spectrum of given level and type, the existence of weights and a permutation statement for Satake parameters, one obtains finitely many isobaric data $D_1, \dots, D_k$ of rank $n$ such that each $D_j$ is a base of $\pi$ (its infinitesimal characters add up to the infinitesimal character of the weight of $\pi$, and it describes $\pi$ at all but finitely many split places, and at the split place of $S$ if there is one) and such that for every finite set $T$ of places some $D_j$ has, at every nonsplit $w \in T$ where $\pi$ is unramified, the Satake parameter $\mathrm{bc}_n(\alpha)$ for every Satake parameter $\alpha$ of $\pi$ at $w$.
3. One datum for all places. Some $D_j$ works for every $T$: otherwise each $j$ has a finite set $T_j$ on which it fails, and no $D_j$ works for $T_1 \cup \cdots \cup T_k$, since the condition on $T$ passes to subsets. So there is a full datum $D$: a base of $\pi$ with the inert condition at every unramified nonsplit place. The passage from a full datum to an isobaric base change uses two further statements: two full data have the same Satake parameters at almost all places, and full data are stable under the twist by $\theta$.

The deductions in steps 1 and 2, and this last passage, are proved statements that we did not unfold. $\square$

### The theorem

**Theorem 7.26.4 (Isobaric base change).** Let $E$ be a CM field unramified over $F$, $n \ge 1$, and $\pi$ an automorphic representation of $U(n)$. Then $\pi$ has an isobaric base change.

Lean: `UpperTheory.BaseChangeIdentities.baseChangeN`.

*Proof.* The finiteness of candidates holds. It is deduced from seven proved statements, on finite strict data, strict products, strict joins, the parts of candidates, open levels, inverse isomorphisms and admissible products, which we did not unfold. Apply the conditional form. $\square$

There is a second proof, in which the finiteness of candidates comes from a local statement.

**Definition 7.26.5 (Finiteness of Jacquet eigenvalues).** Finiteness of Jacquet eigenvalues holds if for all isobaric data $P_a$, $P_b$ of ranks $a$, $b$, every finite place $w$ and every uniformizer $\varpi$ of $E_w$, there are a finite set $Z$ and $m \ge 0$ such that for all $P'_a$, $P'_b$ equivalent to $P_a$, $P_b$, the Iwahori fixed vectors of the local product of $P'_a$ and $P'_b$ at $w$ have dimension at most $m$, and every Jacquet eigenvalue of $(P'_a, P'_b)$ at $w$, in the sense of Section 25, lies in $Z$.

**Theorem 7.26.6 (Isobaric base change, second proof).** The conclusion of the theorem above holds, with the finiteness of candidates obtained from the finiteness of Jacquet eigenvalues, which is proved, and with the reading of characters and the limit statement for infinitesimal characters taken in a second form.

Lean: `UpperTheory.BaseChangeIdentities.baseChangeNB`.

*Proof.* Finiteness of Jacquet eigenvalues gives the finiteness of candidates, by a proved reduction that we did not unfold. The rest is the proof of the conditional form, with two inputs replaced: the limit statement is [the one of Section 08](/entry/e-final-of/), proved from the separation of spectra, the finiteness of discrete spectra and limits of vectors; and the reading of characters is proved from the block candidates with a second form of the output statement. $\square$

**Remark 7.26.7 (Formalization).** The three theorems are [FillPre.lean](lean:Development/AutomorphicArithmetic/Foundations/BaseChangeIdentities/FillPre.lean#L7), [DefiniteNHolds.lean](lean:Development/AutomorphicArithmetic/Foundations/BaseChangeIdentities/DefiniteNHolds.lean#L5) and [BaseChangeNB.lean](lean:Development/AutomorphicArithmetic/Foundations/BaseChangeIdentities/BaseChangeNB.lean#L7). The statement `BaseChangeIsobaricN` and the structure `IsBaseChangeN` are in BaseChangeIsobaricNOf.lean (lines 39 and 21). `baseChangeN_of` applies `Plug2.bci_of` (SatakeExponents/BciOf.lean:22) to `frameEx_of_fin uSide hCF`, `frameBound` and `GelfandReading.frameRead`. `bci_of` is `fieldN_of_run` (FullThetaHolds.lean:31) of `runFin_chain` (RunFinChain.lean:8) of `genEx_of` (FrameBound.lean:44); step 2 is `RunFin` (FieldNOf.lean:25), and the full data of step 3 are `Full` (line 22), with `FullSat` and `FullTheta`. The pigeonhole argument in step 3 is our reading of how `full_of` (line 37) uses `RunFin`; we did not unfold it. `baseChangeN` applies `baseChangeN_of` to `candFin` (HeckeEigenvalueFiniteness/FrameEx.lean:15), whose file is named for a different statement. `baseChangeNB` uses `Plug2B.bci_of` (BciOfAlt.lean:22), a copy of `bci_of` that differs only in using `eFinal_holds'` (EFinalNEHoldsAlt.lean:9, which is `eFinal_of`) for `eFinal_holds` (EFinalNEHolds.lean:7), with `candFin_of_jEigFin jEigFin` and `frameRead_holdsB` (FinalAllB.lean:33). Both proofs give the same statement. The Speh type condition `CsdAsc` uses `AscEmb` (IsSliceMap.lean:53) with exponents $(a - 1)e_i$, written `-spehExp d i + a * spehExp d i`, while `IsSpehOf` (IsNormalisedOfIsDiscrete.lean:58) uses $(a + 1)e_i$; the two conventions differ, and neither is the usual exponent $e_i$ unless the absolute value is normalized differently. The inert condition 5 is stated for every choice of local conjugation, uniformizer and $q$ satisfying `IsUnramInv`.

## Notes and references

The chapter follows the comparison of the trace formula of a definite unitary group with the twisted trace formula of $\mathrm{GL}_n$ over a CM field, in the form that goes back to [base change](/learn/automorphic-forms/#base-change) for cyclic extensions. Cyclic base change, the matching of orbital integrals and the global comparison of Sections 09 and 10 are in Arthur and Clozel, Chapter 1 for the local and Chapter 3 for the global results. The fundamental lemma for unit elements, used in Sections 04, 09 and 20, is due to Kottwitz. The [twisted trace formula](/learn/trace-formula/#the-twisted-trace-formula-and-base-change) of Sections 06, 07 and 11, with its truncation and its elliptic terms, is in Arthur and Clozel, Chapter 2.

At the finite places, unramified representations and Satake parameters (Sections 03, 15 and 18) go back to Satake; Iwahori fixed vectors and the Iwahori-Matsumoto relations (Sections 03 and 17) are in Iwahori and Matsumoto and in Borel. Jacquet modules, exponents and subquotients of induced representations (Sections 15 and 25) are in Bernstein and Zelevinsky and in Zelevinsky. The factorization of automorphic representations into local components (Section 21) is Flath's theorem. Symmetric functions and Schur polynomials, used in Section 17, are in Macdonald, Chapter I.

At the archimedean places, the Dirac inequality of Section 23 is the inequality of Parthasarathy. The functional equation of Section 24 is that of Godement and Jacquet, and the isobaric representations that appear as base changes, with their uniqueness given the Satake parameters at almost all places, are in Jacquet and Shalika. The discrete spectrum of $\mathrm{GL}_n$ and the Speh representations of Section 26 are described by Mœglin and Waldspurger.

- J. Arthur and L. Clozel, *Simple Algebras, Base Change, and the Advanced Theory of the Trace Formula*, Ann. of Math. Stud. 120, Princeton University Press, 1989, Chapters 1 to 3.
- I. N. Bernstein and A. V. Zelevinsky, Induced representations of reductive p-adic groups I, Ann. Sci. École Norm. Sup. 10 (1977), 441 to 472.
- A. Borel, Admissible representations of a semi-simple group over a local field with vectors fixed under an Iwahori subgroup, Invent. Math. 35 (1976), 233 to 259.
- D. Flath, Decomposition of representations into tensor products, in *Automorphic Forms, Representations and L-functions*, Proc. Sympos. Pure Math. 33, Part 1, Amer. Math. Soc., 1979, 179 to 183.
- R. Godement and H. Jacquet, *Zeta Functions of Simple Algebras*, Lecture Notes in Math. 260, Springer, 1972, §13.
- N. Iwahori and H. Matsumoto, On some Bruhat decomposition and the structure of the Hecke rings of p-adic Chevalley groups, Publ. Math. IHÉS 25 (1965), 5 to 48.
- H. Jacquet and J. A. Shalika, On Euler products and the classification of automorphic representations I, Amer. J. Math. 103 (1981), 499 to 558; II, Amer. J. Math. 103 (1981), 777 to 815.
- R. E. Kottwitz, Base change for unit elements of Hecke algebras, Compositio Math. 60 (1986), 237 to 250.
- I. G. Macdonald, *Symmetric Functions and Hall Polynomials*, 2nd ed., Oxford University Press, 1995, Chapter I.
- C. Mœglin and J.-L. Waldspurger, Le spectre résiduel de GL(n), Ann. Sci. École Norm. Sup. 22 (1989), 605 to 674.
- R. Parthasarathy, Dirac operator and the discrete series, Ann. of Math. 96 (1972), 1 to 30.
- I. Satake, Theory of spherical functions on reductive algebraic groups over p-adic fields, Publ. Math. IHÉS 18 (1963), 5 to 69.
- A. V. Zelevinsky, Induced representations of reductive p-adic groups II, Ann. Sci. École Norm. Sup. 13 (1980), 165 to 210.
